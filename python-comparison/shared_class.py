from multiprocessing.managers import ValueProxy


class SharedClass:
    def __init__(self):
        self.shared_counter = 0

    def increment(self):
        self.shared_counter += 1


class SharedClassDeluxe:
    def __init__(self, shared_counter: ValueProxy):
        self.shared_counter = shared_counter

    def increment(self):
        self.shared_counter.value += 1
