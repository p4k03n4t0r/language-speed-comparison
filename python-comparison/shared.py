from result import Result
from shared_class import SharedClass, SharedClassDeluxe
import timed
from typing import List
import work
from threading import Thread
from multiprocessing import Manager, Process

import time


def multi_thread_func(total_work: int, concurrent: int, shared_class: SharedClass):
    divided_work = int(total_work / concurrent)
    threads = []
    for _ in range(concurrent):
        threads.append(
            Thread(
                target=work.work_shared,
                args=(
                    divided_work,
                    shared_class,
                ),
            )
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def multi_processing_func(total_work: int, concurrent: int, shared_class: SharedClass):
    divided_work = int(total_work / concurrent)
    processes = []
    for _ in range(concurrent):
        process = Process(
            target=work.work_shared,
            args=(
                divided_work,
                shared_class,
            ),
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


# Runs using a shared (pointer to a) variable
def shared(total_work: int, concurrent: int) -> List[Result]:
    results = []

    shared_class = SharedClass()
    results.append(
        timed.timed_shared(
            total_work,
            concurrent,
            "Shared-SingleThreaded",
            shared_class,
            lambda total_work, _, shared_class: work.work_shared(
                total_work, shared_class
            ),
        )
    )

    shared_class = SharedClass()
    results.append(
        timed.timed_shared(
            total_work,
            concurrent,
            "Shared-Multithreaded",
            shared_class,
            multi_thread_func,
        )
    )

    manager = Manager()
    shared_class = SharedClassDeluxe(manager.Value("i", 0))
    results.append(
        timed.timed_shared(
            total_work,
            concurrent,
            "Shared-Multiprocessing",
            shared_class,
            multi_processing_func,
        )
    )
    print(shared_class.shared_counter.value)

    return results
