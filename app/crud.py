from sqlalchemy.orm import Session
from . import models

def create_user(db: Session, name: str, email: str):
    user = models.User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_translation(db: Session, data: dict):
    translation = models.Translation(**data)
    db.add(translation)
    db.commit()
    db.refresh(translation)
    return translation
