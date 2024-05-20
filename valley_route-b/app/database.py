"""
This module contains the database configuration and session management. In this module,
we define the SQLAlchemy engine, session, and base class for the database models.
We also define the database URL in the config module and import it here to create the engine.
"""

# Standard library imports

# Third-party imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Local imports (project-specific)
from config import DATABASE_URL

# Create the SQLAlchemy engine, which is used to connect to the database
engine = create_engine(DATABASE_URL)

# Create a session class for the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the database models
Base = declarative_base()
