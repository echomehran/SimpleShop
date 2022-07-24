from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Product
from utils import format


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/")
async def root():
    return {"message": "Welcome to SIMPLESHOP | INVENTORY."}


@app.get("/products")
async def get_all_products():
    return [format(pk) for pk in Product.all_pks()]


@app.get("/products/{pk}")
def get_a_product(pk: str):
    return Product.get(pk)


@app.post("/products")
def create_product(product: Product):
    return product.save()


@app.delete("/products/{pk}")
def delete_product(pk: str):
    return Product.delete(pk)
