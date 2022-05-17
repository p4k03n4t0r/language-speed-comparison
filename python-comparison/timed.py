from result import Result
import time

from shared_class import SharedClass, SharedClassDeluxe


def timed_isolated(total_work: int, concurrent: int, name: str, call) -> Result:
    start = time.perf_counter_ns()
    call(total_work, concurrent)
    end = time.perf_counter_ns()
    elapsed = end - start
    return Result(name, elapsed, -1)


def timed_returned(total_work: int, concurrent: int, name: str, call) -> Result:
    start = time.perf_counter_ns()
    result = call(total_work, concurrent)
    end = time.perf_counter_ns()
    elapsed = end - start
    return Result(name, elapsed, result)


def timed_shared(
    total_work: int, concurrent: int, name: str, shared_class, call
) -> Result:
    start = time.perf_counter_ns()
    call(total_work, concurrent, shared_class)
    end = time.perf_counter_ns()
    elapsed = end - start

    if isinstance(shared_class, SharedClassDeluxe):
        result = shared_class.shared_counter.value
    elif isinstance(shared_class, SharedClass):
        result = shared_class.shared_counter
    else:
        raise TypeError(shared_class)
    return Result(name, elapsed, result)
