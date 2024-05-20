"""
This module contains the SQLAlchemy model classes for the database entities.

SQLAlchemy is an Object-Relational Mapping (ORM) library for Python that provides a way to
interact with databases using Python objects.

In this module, we define the following model classes:
User: Represents a user entity in the database.
Node: Represents a node entity in the database.
Edge: Represents an edge entity in the database.
Package: Represents a package entity in the database.
"""

# Standard library imports
from datetime import datetime

# Third-party imports
from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Local imports (project-specific)
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

    # Define the table name for the User model
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    firstName = Column(String(100))
    lastName = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)

    # Define the relationship between the User and Package models
    packages = relationship("Package", back_populates="owner")


class Node(Base):
    """
    Represents a node entity in the database. Nodes are used to represent locations on a map as checkpoints.

    Attributes:
    - id (int): The unique identifier for the node (primary key).
    - name (str): The name of the node.
    - lat (float): The latitude coordinate of the node.
    - lng (float): The longitude coordinate of the node.

    """

    # Define the table name for the Node model
    __tablename__ = "node"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    lat = Column(Float(20))
    lng = Column(Float(20))


class Edge(Base):
    """
    Represents an edge entity in the database. Edges are used to represent connections between nodes in a graph.

    Attributes:
    - id (int): The unique identifier for the edge (primary key).
    - node_from (int): The id of the node where the edge starts.
    - node_to (int): The id of the node where the edge ends.
    - distance (float): The distance between the two nodes connected by the edge.

    """

    # Define the table name for the Edge model
    __tablename__ = "edge"

    id = Column(Integer, primary_key=True)
    start_node_id = Column(Integer, ForeignKey('node.id'))
    end_node_id = Column(Integer, ForeignKey('node.id'))
    distance = Column(Float(20))

    # Define the relationship between the Edge and Node models
    start_node = relationship("Node", foreign_keys=[start_node_id])
    end_node = relationship("Node", foreign_keys=[end_node_id])


class Package(Base):
    """
    Represents a package entity in the database.

    Attributes:
    - id (int): The unique identifier for the package (primary key).
    - name (str): The name of the package.
    - user_id (int): The id of the user who owns the package.
    - user (relationship): Many-to-one relationship with User entities, representing the user who owns the package.

    """

    # Define the table name for the Package model
    __tablename__ = "package"

    id = Column(Integer, primary_key=True)
    description = Column(String(100))
    created_at = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey('user.id'))
    start_node_id = Column(Integer, ForeignKey('node.id'))
    end_node_id = Column(Integer, ForeignKey('node.id'))

    # Define the relationship between the Package and User models, and the start and end nodes
    owner = relationship("User", back_populates="packages")
    start_node = relationship("Node", foreign_keys=[start_node_id])
    end_node = relationship("Node", foreign_keys=[end_node_id])
