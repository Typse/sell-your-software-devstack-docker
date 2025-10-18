from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from datamodel.CheckoutData import CheckoutProduct, DisplayProduct
from typing import List
import stripe
import json

stripe.api_key = ''
YOUR_DOMAIN = 'http://localhost:5173'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[YOUR_DOMAIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products", description="Get all products that are listed in the stripe product dashboard")
async def get_products() -> List[DisplayProduct]:
    products = stripe.Product.list()
    prices = stripe.Price.list()

    result: List[DisplayProduct] = []

    for product in products["data"]:
        price = next( (p for p in prices["data"] if p["product"] == product["id"]), None )

        result.append(DisplayProduct(
            product_id = str(product.id),
            product_name = str(product.name),
            product_description = str(product.description),
            price_id = price.id if price else None,
            product_price = price.unit_amount / 100
        ))

    return result 


@app.post("/create-checkout-session", description="Post a list of products the customer wants to buy.")
async def create_checkout_session(checkout_info: List[CheckoutProduct]):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, price_1234) of the product you want to sell
                    'price': 'price_1SJTgF4OiZoMUwCEZZNAlhjq',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return RedirectResponse(url=checkout_session.url, status_code=303)
