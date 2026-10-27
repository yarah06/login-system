from database import SessionLocal, engine
from models import User
from sqlalchemy.orm import joinedload

engine.echo = True

db = SessionLocal()
users = db.query(User).options(joinedload(User.user_roles)).all()

print('--- Now accessing user_roles for each user ---')
for u in users:
    print(u.email, '->', u.user_roles)

db.close()