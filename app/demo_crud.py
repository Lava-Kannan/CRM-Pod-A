from app.database import SessionLocal
from app import crud
from app.models import User,Contact # for queries


# open db session
db = SessionLocal()

# -------------------
# CREATE USER
# -------------------
new_user = crud.create_user(
    db,
    name="Alice",
    email="alice@example.com",
    hashed_password="secret123"
)
print("✅ Created User:", new_user.id, new_user.name, new_user.email)

# -------------------
# CREATE CONTACTS
# -------------------
contact1 = crud.create_contact(
    db,
    owner_id=new_user.id,
    name="Bob Smith",
    phone="1234567890",
    email="bob@example.com"
)

contact2 = crud.create_contact(
    db,
    owner_id=new_user.id,
    name="Charlie Brown",
    phone="9876543210",
    email="charlie@example.com"
)

print("✅ Added Contacts:", contact1.name, ",", contact2.name)

# -------------------
# GET CONTACTS
# -------------------
contacts = crud.get_contacts_for_user(db, new_user.id)
print("📌 Contacts for", new_user.name, ":", [c.name for c in contacts])

# -------------------
# GET ALL USERS
# -------------------
all_users = crud.get_all_users(db)
print("📌 All Users:", [u.email for u in all_users])

# -------------------
# GET ALL CONTACTS
# -------------------
all_contacts = crud.get_all_contacts(db)
print("📌 All Contacts:", [(c.name, c.email) for c in all_contacts])

# close db session
db.close()
