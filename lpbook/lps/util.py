
class DynamicInterval:
    def __init__(self, min_interval, max_interval, increase_factor=1.1, decrease_factor=2):
        self.min_interval = min_interval
        self.max_interval = max_interval
        self.cur_interval = min_interval
        self.decrease_factor = decrease_factor
        self.increase_factor = increase_factor

    def increase(self):
        self.cur_interval = min(self.max_interval, self.cur_interval * self.increase_factor)

    def decrease(self):
        self.cur_interval = max(self.min_interval, self.cur_interval // self.decrease_factor)
    
