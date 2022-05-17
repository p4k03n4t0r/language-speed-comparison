from shared import SharedClass


def work(max: int) -> int:
    counter = 0
    for _ in range(max):
        counter += 1
    return counter


def work_shared(max: int, shared_class: SharedClass):
    for _ in range(max):
        shared_class.increment()
