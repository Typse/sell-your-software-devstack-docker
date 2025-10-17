from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.db import get_session
from pydantic import BaseModel

router = APIRouter(tags=["customers"])

class CustomerCreate(BaseModel):
    """Wordpress -> Daten"""
    name: str
    age: int
    email: str
    country: str
    post_code: int
    town: str
    street: str
    street_nr: int
    currency: str

class CustomerResponse(BaseModel):
    """API -> Daten"""
    id: int
    name: str
    age: int
    email: str
    country: str
    post_code: int
    town: str
    street: str
    street_nr: int
    currency: str

@router.get("/customers")
async def get_customers(session: AsyncSession = Depends(get_session)):
    """Hole alle Customers"""
    result = await session.execute(text("SELECT * FROM Customers"))
    rows = [dict(r) for r in result.mappings().all()]
    return {"customers": rows}

@router.post("/customers")
async def add_customer(data: CustomerCreate, session: AsyncSession = Depends(get_session)):
    """Erstelle neuen Customer (WORDPRESS)"""
    await session.execute(text("""
        INSERT INTO Customers (name, age, email, country, post_code, town, street, street_nr, currency)
        VALUES (:name, :age, :email, :country, :post_code, :town, :street, :street_nr, :currency)
    """), data.model_dump())
    await session.commit()
    return {"status": "ok", "email": data.email}