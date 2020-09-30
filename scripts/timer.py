import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None
        self._total_time = None

    def start(self):
        if self._start_time is not None:
            return

        self._start_time = time.perf_counter()
        self._total_time = self._start_time

    def stop(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        self._total_time += time.perf_counter() - self._start_time
        self._start_time = None

    def get_time(self):
        if not self._total_time:
            return 0.0
        elif not self._start_time:
            return self._total_time + time.perf_counter()
        else:
            return self._total_time + time.perf_counter() - self._start_time
