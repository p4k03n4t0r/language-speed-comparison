from result import Result
from shared_class import SharedClass
import timed
from typing import List
import work

# Runs using a shared (pointer to a) variable
def shared(total_work: int, concurrent: int) -> List[Result]:
    results = []
    divided_work = total_work / concurrent

    shared_class = SharedClass()
    results.append(
        timed.timed_shared(
            total_work,
            concurrent,
            "Isolated-SingleThreaded",
            shared_class,
            lambda total_work, _: work.work_shared(total_work, shared_class),
        )
    )

    return results
