# Import standard modules

# Import third party modules
# Import numpy library for adjacency matrix operations
import numpy as np
# Import pandas library for data manipulation
from scipy.sparse.csgraph import shortest_path


class SearchPath:
    def __init__(self, edges_graph):
        self.matrix = None
        self.predecessors = None
        self.distances = None
        self.edges_graph = edges_graph
        self.calculate_matrix_adjacency()
        self.calculate_pr_dist()

    def calculate_matrix_adjacency(self):
        """
        Calculates the adjacency matrix of the graph.

        Returns:
        - pd.DataFrame: The adjacency matrix of the graph.
        """

        self.matrix = np.zeros((len(self.edges_graph), len(self.edges_graph)))

        for index, row in self.edges_graph.iterrows():
            from_node = row['nodeFrom']
            to_node = row['nodeTo']
            distance = row['distance']
            self.matrix[from_node][to_node] = distance
            self.matrix[to_node][from_node] = distance

    def calculate_pr_dist(self, directed=False, method='D', return_predecessors=True, start=0, end=0):
        """
        Calculates the shortest path in the graph.

        Args:
        - directed (bool): Indicates whether the graph is directed or not.
        - method (str): The method to use for calculating the shortest path.
        - return_predecessors (bool): Indicates whether to return the predecessors of the shortest path.

        Returns:
        - np.array: The shortest path in the graph.
        - np.array: The predecessors of the shortest path.
        """

        # Calculate de distance and predecessors matrix of the graph
        distance, predecessors = shortest_path(self.matrix, directed=directed, method=method,
                                               return_predecessors=return_predecessors)

        self.predecessors = predecessors
        self.distances = distance

    def get_path(self, start, end):
        """
        Gets the path between two nodes.

        Args:
        - predecessors (np.array): The predecessors of the shortest path.
        - start (int): The starting node.
        - end (int): The ending node.

        Returns:
        - list: The path between the two nodes.
        - float: The distance of the path.
        """

        path = [end]

        # Get the path between the two nodes start from the end
        while self.predecessors[start, end] != -9999:
            path.append(self.predecessors[start, end])
            end = self.predecessors[start, end]

        # Reverse the path to get the correct order
        path.reverse()

        return path, self.distances[start, end]
