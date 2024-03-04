from prometheus_client import Counter, Summary


refresh_driver_error = Counter('lpbook_refresh_driver_error', 'Driver refresh errors.', ['protocol'])
lps_trading_tokens_time = Summary('lpbook_lps_trading_tokens_time', 'Time for serving lps_trading_tokens endpoint.')