from database import SessionLocal
from models import User, Role, UserRole
from auth import hash_password

db = SessionLocal()

test_users = [
    {"full_name": "Ahmed Ali", "email": "ahmed@test.com", "role": "admin"},
    {"full_name": "Sara Mohammed", "email": "sara@test.com", "role": "user"},
    {"full_name": "Khalid Nasser", "email": "khalid@test.com", "role": "user"},
]

for u in test_users:
    existing_user = db.query(User).filter(User.email == u["email"]).first()
    if existing_user is not None:
        print(f"User already exists, skipping: {u['email']}")
        continue

    new_user = User(
        full_name=u["full_name"],
        email=u["email"],
        hashed_password=hash_password("Test1234!"),
    )
    db.add(new_user)
    db.flush()

    role = db.query(Role).filter(Role.name == u["role"]).first()
    new_user_role = UserRole(user_id=new_user.id, role_id=role.id)
    db.add(new_user_role)

    print(f"Added user: {u['email']} with role: {u['role']}")

db.commit()
db.close()