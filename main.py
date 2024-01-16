from queue import Queue

from queue_worker import QueueWorker
from thread_worker import ThreadWorker

if __name__ == "__main__":
    thread_worker = ThreadWorker()
    thread_worker.put_command(lambda: 1 / 0)
    thread_worker.put_command(lambda: print('Hello!'))
    thread_worker.run()
