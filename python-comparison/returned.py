from result import Result
import timed
from typing import List
import work

# Runs and processes the result
def returned(total_work: int, concurrent: int) -> List[Result]:
    results = []
    divided_work = total_work / concurrent

    results.append(
        timed.timed_returned(
            total_work,
            concurrent,
            "Returned-SingleThreaded",
            lambda total_work, concurrent: work.work(total_work),
        )
    )

    return results
