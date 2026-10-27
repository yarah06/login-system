from database import SessionLocal
from models import Role

db = SessionLocal()

default_roles = ["admin", "user"]

for role_name in default_roles:
    existing_role = db.query(Role).filter(Role.name == role_name).first()
    if existing_role is None:
        new_role = Role(name=role_name)
        db.add(new_role)
        print(f"Added role: {role_name}")
    else:
        print(f"Role already exists, skipping: {role_name}")

db.commit()
db.close()