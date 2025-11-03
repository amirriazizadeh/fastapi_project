from fastapi import APIRouter
from sqlmodel import select
from dependencies import SessionDep
from models.users import User


router = APIRouter()


@router.post("/user")
def create_user(user: User, session: SessionDep) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

