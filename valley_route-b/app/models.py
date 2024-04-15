from sqlalchemy import Column, Integer, String, Boolean

from app.database import Base


class User(Base):
    """
    Represents a user entity in the database.

    Attributes:
    - id (int): The unique identifier for the user (primary key).
    - email (str): The email address of the user (unique).
    - name (str): The name of the user.
    - hashed_password (str): The hashed password of the user.
    - is_active (bool): Indicates whether the user account is active (default is True).
    - tasks (relationship): One-to-many relationship with Task entities, representing tasks owned by the user.

    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    firstName = Column(String(100))
    lastName = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)
