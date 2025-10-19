from pydantic import BaseModel
from typing import Optional

class CheckoutProduct(BaseModel):
    """
    Das ist so dumm, dass 'product_id' und 'price_id' string sein muessen...
    """
    product_id: str 
    price_id: str 
    product_name: str
    product_price: float
    product_quantity: int


class DisplayProduct(BaseModel):
    product_id: str 
    price_id: str 
    product_name: str
    product_price: float
    product_description: str
