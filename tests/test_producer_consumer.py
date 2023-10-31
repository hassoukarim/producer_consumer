import numpy as np
import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../producer_consumer"))
sys.path.append(root_dir)

from producer_consumer.producer_consumer import ProducerConsumer

def test_producer_consumer():
    prod_cons = ProducerConsumer(100, 100_000)
    prod_cons.run()
    assert len(prod_cons.consumer.consumed_data) == 100_000
    assert len(prod_cons.buffer) == 0
    assert (prod_cons.consumer.consumed_data["product_id"].sort_values() == np.arange(100_000)).all()