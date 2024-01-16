from queue import Queue


class State:
    def handle(self, command):
        pass


class NormalState(State):
    def __init__(self, queue_worker):
        self.queue_worker = queue_worker

    def handle(self, command):
        if command == "HardStop":
            return None
        elif command == "MoveToCommand":
            return MoveToState(self.queue_worker)
        else:
            # Обработка обычной команды
            command()
            return self


class MoveToState(State):
    def __init__(self, queue_worker):
        self.queue_worker = queue_worker
        self.move_queue = Queue()

    def handle(self, command):
        if command == "HardStop":
            return None
        elif command == "RunCommand":
            return NormalState(self.queue_worker)
        else:
            # Обработка команды MoveToCommand
            self.move_queue.put(command)
            return self

