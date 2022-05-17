from result import Result
import timed
from typing import List
import work

# Runs and processes the result
def returned(total_work: int, concurrent: int) -> List[Result]:
    results = []

    results.append(
        timed.timed_returned(
            total_work,
            concurrent,
            "Returned-SingleThreaded",
            lambda total_work, concurrent: work.work(total_work),
        )
    )

    # results.append(
    #     timed.timed_isolated(
    #         total_work, concurrent, "Returned-Multithreaded", multi_thread_func
    #     )
    # )

    # results.append(
    #     timed.timed_isolated(
    #         total_work, concurrent, "Returned-Multiprocessing", multi_processing_func
    #     )
    # )

    return results
