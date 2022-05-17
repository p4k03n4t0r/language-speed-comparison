from result import Result
import time

from shared_class import SharedClass


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
    total_work: int, concurrent: int, name: str, shared_class: SharedClass, call
) -> Result:
    start = time.perf_counter_ns()
    result = call(total_work, concurrent)
    end = time.perf_counter_ns()
    elapsed = end - start
    return Result(name, elapsed, shared_class.shared_counter)
