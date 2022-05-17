class Result:
    def __init__(self, name: str, time: int, total_count: int):
        self.name = name
        self.time = time / 1000000  # nanosecond to milisecond conversion
        self.total_count = total_count

    def __str__(self) -> str:
        return f"{self.name} {self.time}ms ({self.total_count})"
