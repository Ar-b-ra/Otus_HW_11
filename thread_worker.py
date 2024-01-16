import threading
from queue import Queue
from typing import Callable

from queue_worker import QueueWorker
from utility.custom_logger import root_logger


class ThreadWorker:
    def __init__(self):
        self.event = threading.Event()
        self.queue_worker = QueueWorker(Queue(), self.event)
        self.event.set()
        self.thread = threading.Thread(target=self.queue_worker.run)

    def hard_stop(self):
        self.queue_worker.stop()
        self.thread.join()

    def soft_stop(self):
        self.thread.join()

    def run(self):
        self.queue_worker.is_working = True
        self.thread.start()

    def put_command(self, item: Callable):
        root_logger.debug(f'Put_command: {item}')
        self.queue_worker.put_command(item)
