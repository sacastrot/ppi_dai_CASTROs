"""
This module defines the main FastAPI application and the endpoints for the API.

"""

# Standard library imports

# Third-party imports
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Annotated

# Local imports (project-specific)
from app import auth, crud, models, schemas
from app.database import SessionLocal, engine

# Create the FastAPI application instance
app = FastAPI()

# Include the routers for the authentication endpoints
app.include_router(auth.router)

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Configure the CORS middleware to allow requests from any origin
origins = ['*']

# Add the CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    """
    Dependency to get a database session.

    Args:
    - None

    Returns:
    - Session: A SQLAlchemy session to the database.

    Yields:
    - Session: A SQLAlchemy session to the database.
    """

    # Create a new session for each request
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Define the dependencies for the database session and the current user
db_dependency = Annotated[Session, Depends(get_db)]

# Define the dependency for the current user
user_dependency = Annotated[schemas.User, Depends(auth.get_current_user)]


@app.get("/", tags=["User"], status_code=status.HTTP_200_OK, response_model=schemas.UserBase)
async def get_user(user: user_dependency, db: db_dependency):
    """
    Get the current user.
    Args:
        user: (schemas.User) The current user.
        db: (Session) The database session.

    Returns:
        schemas.UserBase: The current user.

    """
    if user is None:
        # If the user is not authenticated, return an HTTP 401 Unauthorized response
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    return user


@app.post("/node/", tags=["Nodes"], status_code=status.HTTP_201_CREATED, response_model=schemas.Node)
async def create_node(user: user_dependency, node: schemas.NodeCreate, db: db_dependency):
    """
    Create a new node.
    Args:
        user: (schemas.User) The current user.
        node: (schemas.NodeCreate) The data for the new node.
        db: (Session) The database session.

    Returns:
        schemas.Node: The new node.
    """
    if user is None:
        # If the user is not authenticated, return an HTTP 401 Unauthorized response
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    return crud.new_node(db, node)


@app.get("/node/", tags=["Nodes"], status_code=status.HTTP_200_OK)
async def get_node_all(user: user_dependency, db: db_dependency):
    """
    Get all nodes.
    Args:
        user: (schemas.User) The current user.
        db: (Session) The database session.

    Returns:
        List[schemas.Node]: A list of all nodes.
    """
    if user is None:
        # If the user is not authenticated, return an HTTP 401 Unauthorized response
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    return crud.get_node_all(db)


@app.post("/edge/", tags=["Edges"], status_code=status.HTTP_201_CREATED, response_model=schemas.Edge)
async def create_edge(user: user_dependency, edge: schemas.EdgeCreate, db: db_dependency):
    """
    Create a new edge.
    Args:
        user: (schemas.User) The current user.
        edge: (schemas.EdgeCreate) The data for the new edge.
        db: (Session) The database session.

    Returns:
        schemas.Edge: The new edge.

    """
    if user is None:
        # If the user is not authenticated, return an HTTP 401 Unauthorized response
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    return crud.new_edge(db, edge)


@app.get("/edge/", tags=["Edges"], status_code=status.HTTP_200_OK)
async def get_edge_all(user: user_dependency, db: db_dependency):
    """
    Get all edges.
    Args:
        user: (schemas.User) The current user.
        db: (Session) The database session.

    Returns:
        List[schemas.Edge]: A list of all edges.
    """
    if user is None:
        # If the user is not authenticated, return an HTTP 401 Unauthorized response
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    return crud.get_edge_all(db)


@app.post("/package/", tags=["Packages"], status_code=status.HTTP_201_CREATED, response_model=schemas.PackageCreate)
async def create_package(user: user_dependency, package: schemas.PackageCreate, db: db_dependency):
    """
    Create a new package.
    Args:
        user: (schemas.User) The current user.
        package: (schemas.PackageCreate) The data for the new package.
        db: (Session) The database session.

    Returns:
        schemas.PackageCreate: The new package.
    """
    if user is None:
        # If the user is not authenticated, return an HTTP 401 Unauthorized response
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    return crud.create_user_package(db, user.id, package)


@app.get("/package/{package_id}", tags=["Packages"], status_code=status.HTTP_200_OK)
async def get_package(package_id: int, db: db_dependency):
    """
    Get a package by ID.
    Args:
        package_id: (int) The ID of the package to retrieve.
        db: (Session) The database session.

    Returns:
        schemas.Package: The package with the specified ID.
    """
    response = crud.get_package(db, package_id)

    if response is None:
        # If the package is not found, return an HTTP 404 Not Found response
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found")

    return response


@app.get("/packages", tags=["Packages"], status_code=status.HTTP_200_OK)
async def get_all_package(user: user_dependency, db: db_dependency, page: int = 1):
    """
    Get all packages for the current user.
    Args:
        user: (schemas.User) The current user.
        db: (Session) The database session.
        page: (int) The page number for the paginated results.

    Returns:
        List[schemas.Package]: A list of all packages for the current user.
    """
    if user is None:
        # If the user is not authenticated, return an HTTP 401 Unauthorized response
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    return crud.get_all_packages(db, user.id, page)


@app.get("/statistics/nodestart", tags=["Statistics"], status_code=status.HTTP_200_OK)
async def get_statistics_nodestart(db: db_dependency):
    """
    Get statistics for the start nodes of packages.
    Args:
        db: (Session) The database session.

    Returns:
        List[dict]: A list of dictionaries containing the start node statistics.
    """

    return crud.get_package_by_start_node(db)


@app.get("/statistics/nodeend", tags=["Statistics"], status_code=status.HTTP_200_OK)
async def get_statistics_nodeend(db: db_dependency):
    """
    Get statistics for the end nodes of packages.
    Args:
        db: (Session) The database session.

    Returns:
        List[dict]: A list of dictionaries containing the end node statistics.

    """
    return crud.get_package_by_end_node(db)
