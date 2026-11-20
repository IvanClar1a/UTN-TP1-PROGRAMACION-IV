from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field


class UserBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)


class User(UserBase):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    is_active: bool = True


class UserUpdate(UserBase):
    name: str = Field(..., min_length=1)
    is_active: bool


class UserPatch(UserBase):
    name: Optional[str] = Field(None, min_length=1)
    is_active: Optional[bool] = None


class GetUsersResponse(BaseModel):
    users: List[User]


class CreateUserResponse(BaseModel):
    message: str
    user: User


class UpdateUserResponse(BaseModel):
    message: str
    user: User


class DeleteUserResponse(BaseModel):
    message: str