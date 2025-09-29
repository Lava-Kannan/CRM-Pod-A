# create_user_test.py
from app.database import SessionLocal
from app import models

def create_test_user():
    db = SessionLocal()
    try:
        # Make sure email is unique; change value if this email already exists
        test_user = models.User(email="db_test@example.com", hashed_password=None)
        db.add(test_user)
        db.commit()
        db.refresh(test_user)
        print("Created user:", test_user.id, test_user.email, test_user.created_at)
    except Exception as e:
        print("Error creating user:", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_test_user()
