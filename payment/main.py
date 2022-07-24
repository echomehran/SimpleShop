from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks

from starlette.requests import Request
import requests

from models import Order
from utils import order_completed


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/")
async def root():
    return {"message": "Welcome to SIMPLESHOP | PAYMENT."}


@app.get("/orders/{pk}")
def get_order(pk: str):
    return Order.get(pk)


@app.post('/orders')
async def create_order(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()
    req = requests.get(f"http://localhost:8000/products/{body['id']}")
    product = req.json()

    order = Order(
        product_id=body['id'],
        price=product['price'],
        fee=0.2 * product['price'],
        total=1.2 * product['price'],
        quantity=body['quantity'],
        status='pending'
    )
    order.save()

    background_tasks.add_task(order_completed, order)

    return order
