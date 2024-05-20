"""
This module contains the authentication logic for the FastAPI application.
It includes the following:
- A router instance for the authentication endpoints
- A function to create a new user
- A function to authenticate a user and generate an access token
- A function to reset a user's password
- A function to authenticate a user and generate an access token
- A function to get the current user from the access token
"""

# Standard library imports
from datetime import datetime, timedelta
from typing import Annotated

# Third-party imports
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from starlette import status

# Local imports (project-specific)
from app.database import SessionLocal
from app.models import User
from app.schemas import UserReset

# Create an APIRouter instance
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

# Define the secret key and algorithm to use for encoding and decoding JWT tokens
SECRET_KEY = "H8LF6snrh4ztn0nGVSE9D6gSYFD3qG-WNkfaxn_F5CU"

# Define the hashing algorithm to use for password hashing
ALGORITHM = "HS256"

# Create instances of the CryptContext and OAuth2PasswordBearer classes
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


class CreateUserRequest(BaseModel):
    """
    Represents the request body for creating a new user.

    Attributes:
    - email (str): The email address of the user.
    - password (str): The password of the user.
    - firstName (str): The first name of the user.
    - lastName (str): The last name of the user.
    """
    email: str
    password: str
    firstName: str
    lastName: str


class Token(BaseModel):
    """
    Represents the response body for the token endpoint.

    Attributes:
    - access_token (str): The access token.
    - token_type (str): The token type.
    """
    access_token: str
    token_type: str


def get_db():
    """
    Dependency function to get a database session.

    Args:
    - None

    Returns:
    - db (Session): The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Define a dependency to get the database session
db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserRequest, db: db_dependency):
    """
    Create a new user in the database.

    This endpoint creates a new user in the database if the email is not already registered.

    Args:
        user: (CreateUserRequest): The request body containing the user data,
        first name, last name, email, and password.

        db: (Session): The database session.

    Returns:
        None

    Raises:
        HTTPException: (404_BAD_REQUEST) If the email is already registered.
    """

    # Check if the email is already registered
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        # Return an error if the email is already registered
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    # Hash the password
    hashed_password = bcrypt_context.hash(user.password)

    # Create a new user object
    db_user = User(email=user.email, firstName=user.firstName, lastName=user.lastName, hashed_password=hashed_password)

    # Add the user to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    """
    Authenticate a user and generate an access token. This endpoint authenticates a user
    Args:
        form_data: (OAuth2PasswordRequestForm): The form data containing the username and password.
        db: (Session): The database session.

    Returns:
        (Token): The access token and token type.

    Raises:
        HTTPException: (401_UNAUTHORIZED) If the email or password is incorrect.
    """

    # Authenticate the user
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        # Return an error if the email or password is incorrect
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")

    # Generate an access token
    access_token_expires = timedelta(minutes=30)

    # Create a user data dictionary
    user_data = {"sub": form_data.username}

    # Create the access token
    access_token = create_access_token(data=user_data, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/reset-password")
async def reset_password(body: UserReset, db: db_dependency):
    """
    Reset a user's password. This endpoint allows a user to reset their password
    by providing their email address and a new password.
    Args:
        body: (UserReset): The request body containing the user's email and new password.
        db: (Session): The database session.

    Returns:
        (dict): A message indicating that the password was reset successfully.

    Raises:
        HTTPException: (404_NOT_FOUND) If the user is not found.
    """

    # Check if the user exists
    user = db.query(User).filter(User.email == body.email).first()
    if not user:
        # Return an error if the user is not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    # Hash the new password
    hashed_password = bcrypt_context.hash(body.new_password)
    user.hashed_password = hashed_password
    db.commit()
    return {"message": "Password reset successfully"}


def authenticate_user(db: Session, email: str, password: str):
    """
    Authenticate a user. This function authenticates a user by email and password.
    If the user is found and the password is correct, the user object is returned;
    otherwise, False is returned.
    Args:
        db: (Session): The database session.
        email: (str): The email address of the user.
        password: (str): The password of the user.

    Returns:
        (User): The user object if the user is found and
        the password is correct; otherwise, False.

    """
    user = db.query(User).filter(User.email == email).first()

    # Check if the user exists and the password is correct
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta):
    """
    Create an access token. This function creates an access token
    using the provided data and expiration time.
    Args:
        data: (dict): The data to encode in the token.
        expires_delta: (timedelta): The expiration time for the token.

    Returns:
        (str): The access token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    # Add the expiration time to the token data
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency):
    """
    Get the current user from the access token. This function decodes the access token
    and retrieves the user object from the database based on the email address in the token.

    Args:
        token: (str): The access token.
        db: (Session): The database session.

    Returns:
        (User): The user object if the token is valid and the user is found;
        otherwise, an HTTPException is raised.

    Raises:
        HTTPException: (401_UNAUTHORIZED) If the token is invalid or the user is not found.
    """

    # Define an exception to raise if the credentials are invalid
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode the token and get the email address
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            # Raise an exception if the email is not found
            raise credentials_exception
    except JWTError:
        # Raise an exception if the token is invalid
        raise credentials_exception
    # Get the user from the database based on the email address
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        # Raise an exception if the user is not found
        raise credentials_exception
    return user
