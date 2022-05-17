from result import Result
import timed
from typing import List
import work
from threading import Thread
from multiprocessing import Process


def multi_thread_func(total_work: int, concurrent: int):
    divided_work = int(total_work / concurrent)
    threads = []
    for _ in range(concurrent):
        threads.append(Thread(target=work.work, args=(divided_work,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def multi_processing_func(total_work: int, concurrent: int):
    divided_work = int(total_work / concurrent)
    processes = []
    for _ in range(concurrent):
        process = Process(target=work.work, args=(divided_work,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


# Runs without shared variable or a return value
def isolated(total_work: int, concurrent: int) -> List[Result]:
    results = []

    results.append(
        timed.timed_isolated(
            total_work,
            concurrent,
            "Isolated-SingleThreaded",
            lambda total_work, _: work.work(total_work),
        )
    )

    results.append(
        timed.timed_isolated(
            total_work, concurrent, "Isolated-Multithreaded", multi_thread_func
        )
    )

    results.append(
        timed.timed_isolated(
            total_work, concurrent, "Isolated-Multiprocessing", multi_processing_func
        )
    )

    return results
