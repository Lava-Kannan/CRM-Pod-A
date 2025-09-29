from app.database import SessionLocal
from app import crud, models

db = SessionLocal()

# Clear old data
db.query(models.Contact).delete()
db.query(models.User).delete()
db.commit()

# Insert fresh data
for i in range(1, 6):
    user = crud.create_user(
        db,
        name=f"User{i}",
        email=f"user{i}@example.com",
        hashed_password="pass123"
    )
    for j in range(1, 4):
        crud.create_contact(
            db,
            owner_id=user.id,
            name=f"Contact{j} of User{i}",
            phone=f"12345{i}{j}",
            email=f"contact{j}_user{i}@example.com"
        )

db.close()
