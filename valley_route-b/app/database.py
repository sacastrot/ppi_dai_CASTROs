"""
This module contains the database configuration and session management. In this module,
we define the SQLAlchemy engine, session, and base class for the database models.
We also define the database URL in the config module and import it here to create the engine.
"""

# Standard library imports
import os
from os.path import join, dirname

# Third-party imports
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file or environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Get the database connection details from environment variables

# name of the database
db_name = os.getenv("DATABASE_NAME")

# username for the database
db_user = os.getenv("DATABASE_USER")

# password for the database
db_password = os.getenv("DATABASE_PASSWORD")

# host for the database
db_host = os.getenv("DATABASE_HOST")

# port for the database
db_port = os.getenv("DATABASE_PORT")

# The database URL is in the format "dialect+driver://username:password@host:port/database"
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

# Create the SQLAlchemy engine, which is used to connect to the database
engine = create_engine(DATABASE_URL)

# Create a session class for the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the database models
Base = declarative_base()
