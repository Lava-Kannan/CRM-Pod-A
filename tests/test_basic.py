import pytest
from app.database import SessionLocal
from app import crud

@pytest.fixture
def db_session():
    """Provides a fresh database session for each test."""
    db = SessionLocal()
    yield db
    db.close()

import uuid

def test_create_user(db_session):
    random_email = f"testuser_{uuid.uuid4().hex}@example.com"

    users_before = crud.get_all_users(db_session)
    count_before = len(users_before)

    user = crud.create_user(
        db_session,
        name="Test User",
        email=random_email,
        hashed_password="testpass123"
    )

    users_after = crud.get_all_users(db_session)
    count_after = len(users_after)

    assert count_after == count_before + 1
    assert user.email == random_email
