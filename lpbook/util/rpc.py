import asyncio
import aioprocessing

def create_in_another_process(cls, *args, **kwargs):
    request_queue = aioprocessing.AioQueue()
    response_queue = aioprocessing.AioQueue()

    class RemoteProxy:
        def __init__(self):
            super().__init__()

        async def run_loop(self):
            try:
                while True:
                    request = await request_queue.coro_get()
                    if request is not None:
                        attr, args, kwargs = request
                        attr = getattr(self.local_data_processor, attr, None)
                        if attr and callable(attr):
                            if asyncio.iscoroutinefunction(attr):
                                result = await attr(*args, **kwargs)
                            else:
                                result = attr(*args, **kwargs)
                            await response_queue.coro_put(result)
                    else:
                        break
            except asyncio.CancelledError:
                pass

        def run(self):
            self.local_data_processor = cls(*args, **kwargs)
            asyncio.run(self.run_loop())

    class LocalProxy:
        def __init__(self):
            remote_proxy = RemoteProxy()
            self.remote_process = aioprocessing.AioProcess(target=remote_proxy.run)
            self.remote_process.start()
            self.shutdown_called = False

        def __del__(self):
            if not self.shutdown_called:
                request_queue.put(None)
                self.remote_process.join()

        def shutdown(self):
            #shutdown_call = self._wrapped_remote_call("shutdown")
            #await shutdown_call()
            request_queue.put(None)
            self.remote_process.join()
            self.shutdown_called = True

        def __getattr__(self, attr):
            if hasattr(cls, attr):
                if callable(getattr(cls, attr)):
                    return self._wrapped_remote_call(attr)
                else:
                    raise "Accessing data members not supported" # for no reason - it can easily be done as well
            raise AttributeError(attr)

        def _wrapped_remote_call(self, attr):
            async def async_wrapper(*args, **kwargs):
                await request_queue.coro_put((attr, args, kwargs))
                return await response_queue.coro_get()
            def sync_wrapper(*args, **kwargs):
                request_queue.put((attr, args, kwargs))
                return response_queue.get()
            if asyncio.iscoroutinefunction(getattr(cls, attr)):
                return async_wrapper
            else:
                return sync_wrapper
        
    return LocalProxy()
