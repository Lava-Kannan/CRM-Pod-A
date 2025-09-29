# test_db.py

from app.database import Base, engine, get_db


print("Type of Base:", type(Base))

try:
    db = next(get_db())   
    print(" Database session opened successfully")
    db.close()
except Exception as e:
    print(" Database connection failed:", e)

print("Engine:", engine)


