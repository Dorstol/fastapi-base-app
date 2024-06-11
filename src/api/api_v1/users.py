from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud.users import get_all_users
from core.models import db_helper
from core.schemas.users import UserRead, UserCreate

router = APIRouter(
    tags=["Users"],
)


@router.get("/", response_model=list[UserRead])
async def read_users(session: AsyncSession = Depends(db_helper.session_getter)):
    users = await get_all_users(session=session)
    return users


@router.post("/create", response_model=UserRead)
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    user = await create_user(session=session)
    return user
