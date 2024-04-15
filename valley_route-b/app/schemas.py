from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    """
    UserBase is a Pydantic model that defines the fields that are common to both the UserCreate and User models.
    """
    firstName: str
    lastName: str
    email: str


class UserCreate(UserBase):
    """
    UserCreate is a Pydantic model that defines the fields required to create a new user. It inherits from UserBase and
    adds the password field:
    """
    password: str


class User(UserBase):
    """
    User is a Pydantic model that defines the fields for a user entity. It inherits from UserBase and adds the id,
    is_active and items fields:
    """
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)