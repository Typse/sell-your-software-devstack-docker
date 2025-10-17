import asyncio
from sqlalchemy import text
from .db import engine

async def test_connection():
    try:
        async with engine.begin() as conn:
            r = await conn.execute(text("SELECT 1"))
            print("Connection test successful:", r.scalar_one())
    except Exception as e:
        print("Connection test failed:", type(e).__name__, e)
        
if __name__ == "__main__":
    asyncio.run(test_connection())