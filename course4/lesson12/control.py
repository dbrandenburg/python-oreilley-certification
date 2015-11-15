#!/usr/bin/env python3
"""
control.py: Creates queues, starts output and worker processes,
        and pushes inputs into the input queue.
"""
from multiprocessing import Queue, JoinableQueue
from output import OutThread
from worker import WorkerThread
import string
import random
import timeit

if __name__ == "__main__":

    class Control:
        def __init__(self, workers, number_of_chars):
            self._workers = workers
            self._number_of_chars = number_of_chars

        @staticmethod
        def _random_chars(length):
            for i in range(length):
                yield random.choice(string.ascii_letters)

        def __call__(self):
            inq = JoinableQueue(maxsize=int(WORKERS*1.5))
            outq = Queue(maxsize=int(WORKERS*1.5))

            ot = OutThread(WORKERS, outq, sorting=True)
            ot.start()

            for i in range(self._workers):
                w = WorkerThread(inq, outq)
                w.start()

            instring = ''.join(list(self._random_chars(self._number_of_chars)))

            for work in enumerate(instring):
                inq.put(work)
            for i in range(WORKERS):
                inq.put(None)
            inq.join()
            print("Control thread terminating")

    NUMBER_OF_CHARS = 1000
    WORKERS = 10
    control = Control(WORKERS, NUMBER_OF_CHARS)
    print("Time to run program:",
          timeit.timeit("control()", "from __main__ import control", number=1))
