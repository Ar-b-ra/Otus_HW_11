import unittest
from unittest.mock import MagicMock, patch
from state_handlers import MoveToState
from thread_worker import ThreadWorker


class TestStateHandlers(unittest.TestCase):

    def setUp(self):
        self.thread_worker = ThreadWorker()

    def test_move_to_command(self):
        self.thread_worker.put_command("MoveToCommand")
        self.thread_worker.run()
        self.assertTrue(isinstance(self.thread_worker.queue_worker.current_state, MoveToState))

    @patch("queue_worker.QueueWorker.stop")
    def test_hard_stop(self, stop_command):
        self.thread_worker.put_command("HardStop")
        self.thread_worker.run()
        stop_command.assert_called_once()

