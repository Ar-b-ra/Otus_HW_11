import unittest
from queue import Queue
from unittest.mock import MagicMock

from queue_worker import QueueWorker


class TestRun(unittest.TestCase):
    def test_run_with_empty_queue(self):
        # Test when the queue is empty
        queue = Queue()
        obj = QueueWorker(queue)
        obj.run()
        self.assertFalse(obj.is_working)

    def test_run_with_non_empty_queue(self):
        # Test when the queue has items
        queue = Queue()
        mock_func1 = MagicMock()
        mock_func2 = MagicMock()
        queue.put(mock_func1)
        queue.put(mock_func2)
        obj = QueueWorker(queue)
        obj.is_working = True
        obj.run()
        self.assertFalse(obj.is_working)
        mock_func1.assert_called_once()
        mock_func2.assert_called_once()

    def test_run_exception_handling(self):
        # Test exception handling
        queue = Queue()
        queue.put(lambda: 1 / 0)
        obj = QueueWorker(queue)
        obj.run()
        self.assertFalse(obj.is_working)
        # Assert that the exception is logged


if __name__ == '__main__':
    unittest.main()
