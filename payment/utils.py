from models import Order
from database import redis

import time


def order_completed(order: Order):
    time.sleep(3)
    order.status = 'completed'
    order.save()

    redis.xadd('order_completed', order.dict(), '*')
