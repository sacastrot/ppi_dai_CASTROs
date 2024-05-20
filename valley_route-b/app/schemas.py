"""
The schemas module contains Pydantic models that define the structure
of the data that is sent to and received from the API endpoints. These models are used to
validate the data and serialize it to and from JSON format.

Pydantic is a data validation and parsing library for Python that uses type annotations to define
the structure of the data. It provides a way to define data models with type hints and automatically
validate and serialize the data based on these models.
"""

# Third-party imports
from pydantic import BaseModel, ConfigDict

# Local imports (project-specific)
from app.models import Edge


class UserBase(BaseModel):
    """
    UserBase is a Pydantic model that defines the fields that are common to both the UserCreate and User models.

    Attributes:
    - firstName (str): The first name of the user.
    - lastName (str): The last name of the user.
    - email (str): The email address of the user.
    """
    firstName: str
    lastName: str
    email: str


class UserCreate(UserBase):
    """
    UserCreate is a Pydantic model that defines the fields required to create a new user.
    It inherits from UserBase and adds the password field:

    Attributes:
    - password (str): The password of the user.
    """
    password: str


class UserReset(BaseModel):
    """
    UserReset is a model that defines the fields required to reset a user's password.

    Attributes:
    - email (str): The email address of the user.
    - new_password (str): The new password for the user.

    """
    email: str
    new_password: str


class NodeBase(BaseModel):
    """
    NodeBase is a Pydantic model that defines the fields that are common to both the NodeCreate and Node models.

    Attributes:
    - name (str): The name of the node.
    - lat (float): The latitude coordinate of the node.
    - lng (float): The longitude coordinate of the node.

    """
    name: str
    lat: float
    lng: float


class NodeCreate(NodeBase):
    """
    NodeCreate is a Pydantic model that defines the fields required to create a new node. It inherits from NodeBase and
    adds no additional fields.

    Attributes: None
    """
    pass


class Node(NodeBase):
    """
    Node is a Pydantic model that defines the fields for a node entity.
    It inherits from NodeBase and adds the id field:

    Attributes:
    - id (int): The unique identifier for the node.
    """
    id: int

    # Automatically generate the model configuration from the attributes
    model_config = ConfigDict(from_attributes=True)


class EdgeBase(BaseModel):
    """
    EdgeBase is a Pydantic model that defines the fields that are common to both the EdgeCreate and Edge models.

    Attributes:
    - start_node_id (int): The id of the starting node of the edge.
    - end_node_id (int): The id of the ending node of the edge.

    """
    start_node_id: int
    end_node_id: int


class EdgeCreate(EdgeBase):
    """
    EdgeCreate is a Pydantic model that defines the fields required to create a new edge. It inherits from EdgeBase and
    adds no additional fields.

    Attributes: None
    """
    pass


class EdgeGet:
    """
    EdgeCreate is a Pydantic model that defines the fields required to create a new edge. It inherits from EdgeBase and
    adds no additional fields.

    Attributes: None
    """
    def __init__(self, edge: Edge):
        """
        Initialize the EdgeGet object with the data from the given Edge object.
        Args:
            edge: (Edge): The Edge object to get the data from.
        Returns: None
        """
        self.start_node = edge.start_node
        self.end_node = edge.end_node
        self.distance = edge.distance


class Edge(EdgeBase):
    """
    Edge is a Pydantic model that defines the fields for an edge entity.
    It inherits from EdgeBase.

    Attributes: None
    """
    # Automatically generate the model configuration from the attributes
    model_config = ConfigDict(from_attributes=True)

    pass


class PackageBase(BaseModel):
    """
    PackageBase is a Pydantic model that defines the fields that are
    common to both the PackageCreate and Package models.

    Attributes:
    - description (str): The description of the package.
    - start_node_id (int): The id of the starting node of the package.
    - end_node_id (int): The id of the ending node of the package.
    """
    description: str
    start_node_id: int
    end_node_id: int


class PackageCreate(PackageBase):
    """
    PackageCreate is a Pydantic model that defines the fields required to create a new package.
    It inherits from PackageBase and adds no additional fields.

    Attributes: None
    """
    pass


class Package(PackageBase):
    """
    Package is a Pydantic model that defines the fields for a package entity.
    It inherits from PackageBase and adds the id field and the owner_id field:
    """
    id: int
    owner_id: int

    # Automatically generate the model configuration from the attributes
    model_config = ConfigDict(from_attributes=True)


class PackageGet:
    """
    PackageCreate is a Pydantic model that defines the fields required to create a new edge.
    It inherits from EdgeBase and adds no additional fields.

    Attributes: None
    """
    def __init__(self, package: Package, path: list[Node], distance: float):
        """
        Initialize the PackageGet object with the data from the given Package object.
        Args:
            package: (Package): The Package object to get the data from.
            path: (list[Node]): The path between the start and end nodes of the package.
            distance: (float): The distance of the path.

        Returns: None
        """
        self.id = package.id
        self.description = package.description
        self.created_at = package.created_at
        self.start_node = package.start_node
        self.end_node = package.end_node
        self.owner = package.owner
        self.path = path
        self.distance = distance


class PackageGetAll:
    """
    PackageCreate is a Pydantic model that defines the fields required to create a new edge.
    """
    def __init__(self, id: str, description: str, created_at: str, start_node: str, end_node: str):
        """
        Initialize the PackageGet object with the data from the given Package object.
        Args:
            id: (str): The unique identifier for the package.
            description: (str): The description of the package.
            created_at: (str): The date and time when the package was created.
            start_node: (str): The starting node of the package.
            end_node:  (str): The ending node of the package.

        Returns: None
        """
        self.id = id
        self.description = description
        self.created_at = created_at
        self.start_node = start_node
        self.end_node = end_node


class User(UserBase):
    """
    User is a Pydantic model that defines the fields for a user entity. It inherits from
    UserBase and adds the id field:
    """
    id: int
    is_active: bool

    # Automatically generate the model configuration from the attributes
    model_config = ConfigDict(from_attributes=True)
