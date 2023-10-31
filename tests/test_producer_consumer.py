from producer_consumer.producer_consumer import ProducerConsumer

def test_producer_consumer():
    prod_cons = ProducerConsumer(100, 10_000)
    prod_cons.run()
    assert len(prod_cons.consumer.consumed_data) == 10_000
    assert len(prod_cons.buffer) == 0