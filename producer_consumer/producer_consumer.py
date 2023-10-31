from producer_consumer.producer import Producer
from producer_consumer.consumer import Consumer
from threading import Condition

class ProducerConsumer:
    """
        This class starts both the producer and consumer threads.
    """
    def __init__(self, MAX_LEN: int, N: int):
        self.buffer = [] # The shared buffer where the data is dumped and from which data is consumed
        self.condition = Condition() # Conditional lock
        self.producer = Producer(self.buffer, self.condition, MAX_LEN, N)
        self.consumer = Consumer(self.buffer, self.condition)
    def run(self):
        self.producer.start()
        self.consumer.start()
        self.producer.join()
        self.consumer.join()