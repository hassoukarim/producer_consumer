from producer_consumer.producer_consumer import ProducerConsumer

prod_cons = ProducerConsumer(100, 10_000)

if __name__ == "__main__":
    prod_cons.run()