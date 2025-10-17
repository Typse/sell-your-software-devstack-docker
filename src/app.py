from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.db import get_session
from api.customers import router as customers_router

app = FastAPI(title="Dev API")
app.include_router(customers_router)           # /customers (nginx rewrite)
app.include_router(customers_router, prefix="/api")  # direct access /api/customers

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"hello": "world"}

@app.get("/health/db")
async def health_db(session: AsyncSession = Depends(get_session)):
    result = await session.execute(text("SHOW TABLES"))
    return {"db": [row[0] for row in result]}