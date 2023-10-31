from threading import Thread


class Consumer(Thread):
    """
    Defines the Consumer thread class. This class should consume the data generated by the producer
    from the buffer.
    """

    def __init__(self, buffer, condition):
        super().__init__()
        self.buffer = buffer
        self.condition = condition
        self.consumed_data = []

    def run(self):
        """
        Overridern run method called upon using the start method. This method
        consumes dummy data from the buffer.
        """
        while True:
            with self.condition:
                while not self.buffer:
                    self.condition.wait()
                data = self.buffer.pop()
                if data is None:
                    break
                self.consumed_data.append(data)
                self.condition.notify()
