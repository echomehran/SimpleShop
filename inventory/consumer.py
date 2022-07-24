from database import redis
from models import Product

import time


key = 'order_completed'
group = 'inventory-group'

try:
    redis.xgroup_create(key, group)
except Exception as error:
    print("Error:", error)

while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)

        if len(results) != 0:
            for res in results:
                obj = results[0][1][0][1]

                try:
                    product = Product.get(obj['product_id'])
                    product.quantity -= int(obj['quantity'])
                    product.save()

                    print(product, 'PRODUCT')

                except Exception as error:
                    print(f'Order Refunded: {obj["product_id"]}')
                    
                    redis.xadd('order_refunded', obj, '*')

    except Exception as error:
        print("Error:", error)

    time.sleep(1)
