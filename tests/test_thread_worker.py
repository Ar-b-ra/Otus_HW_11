import unittest
from time import sleep
from unittest.mock import MagicMock

from thread_worker import ThreadWorker


class TestThreadWorker(unittest.TestCase):

    def setUp(self):
        self.thread_worker = ThreadWorker()

    def test_soft_stop(self):
        # Test soft_stop
        mock_func1 = MagicMock()
        mock_func2 = MagicMock()
        self.thread_worker.put_command(mock_func1)
        self.thread_worker.put_command(mock_func2)
        self.thread_worker.run()
        self.thread_worker.hard_stop()
        self.assertTrue(self.thread_worker.queue_worker.queue.empty())
        self.assertFalse(self.thread_worker.queue_worker.is_working)
        self.assertFalse(self.thread_worker.event.is_set())

    def test_hard_stop(self):
        # Test hard_stop
        mock_func1 = lambda: sleep(0.1)
        mock_func2 = MagicMock()
        self.thread_worker.put_command(mock_func1)
        self.thread_worker.put_command(mock_func2)
        self.thread_worker.run()
        self.thread_worker.hard_stop()
        self.assertFalse(self.thread_worker.queue_worker.queue.empty())
        self.assertFalse(self.thread_worker.queue_worker.is_working)
