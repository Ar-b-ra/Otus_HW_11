import threading
from queue import Queue
from typing import Callable

from utility.custom_logger import root_logger


class QueueWorker:
    def __init__(self, queue: Queue, event: threading.Event = None):
        self.queue = queue
        self.is_working = False
        self.thread_event = event if event else threading.Event()

    def set_event(self, event: threading.Event):
        self.thread_event = event

    def run(self):
        self.thread_event.set()
        while not self.queue.empty() and self.is_working:
            item = self.queue.get()
            try:
                item()
            except Exception as e:
                root_logger.exception(e)
            self.queue.task_done()
        self.stop()

    def put_command(self, item: Callable):
        self.queue.put(item)

        if self.queue.empty() and not self.is_working:
            self.is_working = True
            self.run()

    def stop(self):
        self.is_working = False
        self.thread_event.clear()
