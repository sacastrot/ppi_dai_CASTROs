"""
This module contains the CRUD (Create, Read, Update, Delete) operations for the application.
It includes the following:
- Functions to interact with the database
- Functions to create, read, update, and delete data
- Functions to perform business logic
- Functions to handle requests and responses
"""

# Standard library imports
import base64
from io import BytesIO

# Third-party imports
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.sparse.csgraph import shortest_path
from shapely.geometry import Point
from sqlalchemy.orm import Session

# Local imports (project-specific)
from app import models, schemas
from app.models import Node
from app.schemas import EdgeGet, PackageGet, PackageGetAll


def get_user_by_email(db: Session, email: str):
    """
    Retrieves a user from the database by email.

    Args:
        db: (Session): The database session.
        email: (str): The email address of the user.

    Returns:
        models.User: The user object corresponding to the provided email address.
    """
    return db.query(models.User).filter(models.User.email == email).first()


def new_node(db: Session, node: schemas.NodeCreate):
    """
    Creates a new node in the database.

    Args:
        db: (Session): The database session.
        node: (schemas.NodeCreate): The node data to create.

    Returns:
        models.Node: The created node object.
    """

    db_node = models.Node(name=node.name, lat=node.lat, lng=node.lng)
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return db_node


def new_edge(db: Session, edge: schemas.EdgeCreate):
    """
    Creates a new edge in the database.

    Args:
        db: (Session): The database session.
        edge: (schemas.EdgeCreate): The edge data to create.

    Returns:
        models.Edge: The created edge object.
    """
    # Get the start and end nodes
    node_start = db.query(models.Node).filter(models.Node.id == edge.start_node_id).first()

    # Get the start and end nodes
    node_end = db.query(models.Node).filter(models.Node.id == edge.end_node_id).first()

    # Calculate the distance between the start and end nodes
    distance = calculate_distance(node_start, node_end)

    # Create the edge object
    db_edge = models.Edge(start_node_id=edge.start_node_id, end_node_id=edge.end_node_id, distance=distance)

    # Add the edge to the database
    db.add(db_edge)
    db.commit()
    db.refresh(db_edge)
    return db_edge


def get_edge_all(db: Session):
    """
    Retrieves all edges from the database.

    Args:
        db: (Session): The database session.

    Returns:
        list[models.Edge]: A list of all edge objects in the database.
    """

    # Get all edges from the database
    all_edges = db.query(models.Edge).all()

    # Create a list of edge objects
    list_edges = [EdgeGet(edge) for edge in all_edges]
    return list_edges


def calculate_distance(node_start: Node, node_end: Node):
    """
    Calculates the distance between two nodes using geopandas.
    Args:
        node_start: (Node): The start node.
        node_end: (Node): The end node.

    Returns:
        float: The distance between the two nodes.
    """

    # Create two points from the node coordinates
    point1 = Point(node_start.lat, node_start.lng)
    point2 = Point(node_end.lat, node_end.lng)

    # Create a GeoDataFrame with the two points
    points_df = gpd.GeoDataFrame({'geometry': [point1, point2]}, crs='EPSG:4686')

    # Convert the GeoDataFrame to EPSG:32633
    points_df = points_df.to_crs('EPSG:32633')

    # Calculate the distance between the two points
    return points_df.distance(points_df.shift())[1]


def create_user_package(db: Session, user_id: int, package: schemas.PackageCreate):
    """
    Creates a new package in the database.

    Args:
        db: (Session): The database session.
        user_id: (int): The ID of the user who owns the package.
        package: (schemas.PackageCreate): The package data to create.

    Returns:
        models.Package: The created package object.
    """
    db_package = models.Package(**package.dict(), user_id=user_id)
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package


def get_package(db: Session, package_id: int):
    """
    Retrieves a package from the database by ID.

    Args:
        db: (Session): The database session.
        package_id: (int): The ID of the package.

    Returns:
        models.Package: The package object corresponding to the provided ID.
    """

    # Get the package from the database
    package = db.query(models.Package).filter(models.Package.id == package_id).first()

    # If the package is not found, return None
    if package is None:
        return None

    # Get the size of the nodes
    size_nodes = db.query(models.Node).count()

    # Create a matrix of zeros with the size of the nodes
    M = np.zeros((size_nodes, size_nodes))

    # Get all edges from the database
    all_edges = db.query(models.Edge).all()

    # Fill the matrix with the distances between the nodes
    for edge in all_edges:
        M[edge.start_node_id][edge.end_node_id] = edge.distance
        M[edge.end_node_id][edge.start_node_id] = edge.distance

    # Get the shortest path between the start and end nodes
    D, Pr = shortest_path(M, directed=False, method='D', return_predecessors=True)

    # Get the path nodes
    path = get_path(Pr, package.start_node_id, package.end_node_id)
    path_nodes = [db.query(models.Node).filter(models.Node.id == int(node_id)).first() for node_id in path]

    # Create the package return object
    package_return = PackageGet(package, path_nodes, D[package.start_node_id, package.end_node_id])

    return package_return


def get_all_packages(db: Session, owner_id: int, page: int):
    """
    Retrieves all packages from the database for a given user.

    Args:
        db: (Session): The database session.
        owner_id: (int): The ID of the user who owns the packages.
        page: (int): The page number to retrieve.

    Returns:
        dict: A dictionary containing the list of packages and the total number of pages.

    """
    # Set the number of packages per page
    size_page = 8

    # Get all packages from the database for the given user
    all_packages = db.query(models.Package).filter(models.Package.user_id == owner_id).all()

    # Calculate the total number of pages
    total_pages = len(all_packages) // size_page + 1

    # Create a list of package objects
    list_packages = []

    # Create a package object for each package and add it to the list
    for package in all_packages:
        package_id = package.id
        description = package.description
        created_at = package.created_at
        start_node_name = db.query(models.Node).filter(models.Node.id == package.start_node_id).first().name
        end_node_name = db.query(models.Node).filter(models.Node.id == package.end_node_id).first().name
        package_str = PackageGetAll(package_id, description, created_at, start_node_name, end_node_name)
        list_packages.append(package_str)

    # Create a response object with the list of packages and the total number of pages
    response = {
        "data": list_packages[page * size_page - size_page: page * size_page],
        "total_pages": total_pages
    }

    return response


def get_node_all(db: Session):
    """
    Retrieves all nodes from the database.

    Args:
        db: (Session): The database session.

    Returns:
        list[models.Node]: A list of all node objects in the database.
    """
    return db.query(models.Node).all()


def get_path(Pr, i, j):
    """
    Gets the path between two nodes using the predecessor matrix.

    Args:
        Pr: (np.array): The predecessor matrix.
        i: (int): The start node.
        j: (int): The end node.

    Returns:
        list[int]: A list of node IDs representing the path between the two nodes.
    """

    # Create a list to store the path
    path = [j]

    # Get the path nodes, starting from the end node
    while Pr[i, j] != -9999:
        path.append(Pr[i, j])
        j = Pr[i, j]

    # Reverse the path to get the correct order
    path.reverse()
    return path


def get_package_by_start_node(db: Session):
    """
    Create a bar chart with the number of packages that start at each node.

    Args:
        db: (Session): The database session.

    Returns:
        str: A base64 encoded image of the bar chart.

    """

    # Get all packages from the database
    all_packages_query = (db.query(models.Package, models.Node.name).
                          join(models.Node, models.Package.start_node_id == models.Node.id).all())

    # Create a DataFrame with the packages and the start nodes
    group_start = pd.DataFrame(all_packages_query, columns=['Package', 'Start Node'])

    # Group the packages by the start node
    group_start = group_start.groupby('Start Node').count()

    # Create a bar chart with the number of packages that start at each node
    plt.figure(figsize=(15, 6))
    plt.bar(group_start.index, group_start['Package'], width=0.5, color='blue')
    plt.xlabel('Nodos')
    plt.ylabel('Número de Paquetes')
    plt.title('Número de Paquetes por Nodo Inicial')
    plt.grid(True)
    plt.tight_layout()

    # Save the plot to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convert the bytes object to a base64 string
    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64


def get_package_by_end_node(db: Session):
    """
    Create a bar chart with the number of packages that end at each node.

    Args:
        db: (Session): The database session.

    Returns:
        str: A base64 encoded image of the bar chart.
    """

    # Get all packages from the database
    all_packages_query = db.query(models.Package, models.Node.name).join(models.Node,
                                                                         models.Package.end_node_id == models.Node.id).all()

    # Create a DataFrame with the packages and the end nodes
    group_end = pd.DataFrame(all_packages_query, columns=['Package', 'End Node'])
    group_end = group_end.groupby('End Node').count()

    # Create a bar chart with the number of packages that end at each node
    plt.figure(figsize=(15, 6))
    plt.bar(group_end.index, group_end['Package'], width=0.5, color='blue')
    plt.xlabel('Nodos')
    plt.ylabel('Número de Paquetes')
    plt.title('Número de Paquetes por Nodo Final')
    plt.grid(True)
    plt.tight_layout()

    # Save the plot to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convert the bytes object to a base64 string
    image_base64 = base64.b64encode(buffer.read()).decode()

    return image_base64
