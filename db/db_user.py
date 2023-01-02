from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser


def create_user(db: Session, request: UserBase):
  new_user = DbUser(
    username = request.username,
    email = request.email,
    password = Hash.bcrypt(request.password)
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def get_all_users(db: Session):
  users = db.query(DbUser).all()
  return users

def get_user(db: Session, id: int):
  user = db.query(DbUser).filter(DbUser.id == id).first()
  return user

def update_user(db: Session, id: int, request: UserBase):
  user = db.query(DbUser).filter(DbUser.id == id)
  if not user.first():
    return False
  user.update({
      DbUser.username: request.username,
      DbUser.email: request.email,
      DbUser.password: Hash.bcrypt(request.password)
  })
  db.commit()
  return 'ok'

def delete_user(db: Session, id: int):
  user = db.query(DbUser).filter(DbUser.id == id)
  if not user.first():
    return False
  user.delete(synchronize_session=False)
  db.commit()
  return 'ok'