from sqlalchemy.orm import Session

from app import models, schemas


def get_user_by_email(db: Session, email: str):
    """
    Retrieves a user from the database by email address.

    :param db: (Session): The database session.
    :param email: (str): The email address of the user to retrieve.

    :return models.User: The user object corresponding to the provided email address.

    Example:
    >>> user = get_user_by_email(db, 'example@emal.com')
    >>> print(user)
    '{
        "id": 1,
        "email": "example@email.com",
        "firstName": "John",
        "lastName": "Doe",
        "is_active": true
    }'
    """
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    """
    Creates a new user in the database.

    :param db:(Session): The database session.
    :param user:(schemas.UserCreate): The user data to create.

    :return models.User: The created user object.
    """

    fake_hashed_password = user.password + "notReallyHashed"
    db_user = models.User(email=user.email, firstName=user.firstName, lastName=user.lastName, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



