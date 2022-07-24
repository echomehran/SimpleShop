from database import redis
from models import Order

import time


key = 'order_refunded'
group = 'payment-group'

try:
    redis.xgroup_create(key, group)
except Exception as error:
    print("Error:", error)

while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)
        
        # print(results[0][1][0][1] if len(results) > 0 else 'None', 'RESULTS')

        if len(results) != 0:
            order = Order.get(results[0][1][0][1]['pk'])
            
            order.status = 'refunded'
            order.save()
            
            print(f'Order Refunded: {results[0][1][0][1]["pk"]}')
            
    except Exception as error:
        print("Error:", error)

    time.sleep(1)
