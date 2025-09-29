# app/crud.py
from sqlalchemy.orm import Session
from app.models import User, Contact


# -------------------
# USER CRUD
# -------------------

def create_user(db: Session, name: str, email: str, hashed_password: str):
    """Create a new user"""
    user = User(name=name, email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    """Fetch user by email"""
    return db.query(User).filter(User.email == email).first()


def get_all_users(db: Session):
    """Get all users"""
    return db.query(User).all()


# -------------------
# CONTACT CRUD
# -------------------

def create_contact(db: Session, owner_id: int, name: str, phone: str = None, email: str = None):
    """Create a new contact for a user"""
    contact = Contact(owner_id=owner_id, name=name, phone=phone, email=email)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def get_all_users(db): 
    return db.query(User).all()


def get_contacts_for_user(db: Session, user_id: int):
    """Fetch all contacts for a given user"""
    return db.query(Contact).filter(Contact.owner_id == user_id).all()


def get_all_contacts(db: Session):
    """Get all contacts"""
    return db.query(Contact).all()



