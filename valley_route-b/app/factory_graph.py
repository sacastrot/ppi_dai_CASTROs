# Imports standard library modules

# Imports third party modules
# Import numpy library for checkpoints operations
import numpy as np
# Import pandas library for data manipulation
import pandas as pd
# Import geopandas library for geospatial data manipulation
import geopandas as gpd
# Import Point class from shapely.geometry for distance calculation
from shapely.geometry import Point

# Imports local modules
from app.checkpoint import Checkpoint


class FactoryGraph:
    """
    Represents the factory graph of the company ValleyRoute, with its checkpoints.

    Attributes:
    - checkpoints (np.ndarray): The array of Checkpoint objects that represent the checkpoints of the factory.
    """

    def __init__(self, checkpoints: np.ndarray[Checkpoint]):
        """
        Initializes a new instance of the FactoryGraph class.

        Args:
        - checkpoints: The array of Checkpoint objects that represent the checkpoints of the factory.
        """
        self.checkpoints = checkpoints
        self.epgs_default = 'EPGS:4686'
        self.epgs_projected = 'EPGS:32633'

    def create_graph(self) -> pd.DataFrame:
        """
        Creates a graph of the factory checkpoints, define edges and calculate distances between them.

        Returns:
        - pd.DataFrame: The graph of the factory checkpoints with distances between them.
        """

        # Create a DataFrame with edges between the checkpoints and their distances
        df_graph = pd.DataFrame({

            # Define start point of the edge
            'nodeFrom': [self.checkpoints[0], self.checkpoints[0], self.checkpoints[2], self.checkpoints[2],
                         self.checkpoints[3], self.checkpoints[5], self.checkpoints[3], self.checkpoints[4],
                         self.checkpoints[5], self.checkpoints[6], self.checkpoints[6], self.checkpoints[6],
                         self.checkpoints[9], self.checkpoints[9], self.checkpoints[9], self.checkpoints[10],
                         self.checkpoints[8], self.checkpoints[7], self.checkpoints[11], self.checkpoints[11],
                         self.checkpoints[13], self.checkpoints[12], self.checkpoints[13], self.checkpoints[13],
                         self.checkpoints[14], self.checkpoints[14], self.checkpoints[16], self.checkpoints[16],
                         self.checkpoints[16], self.checkpoints[18]],

            # Define end point of the edge
            'nodeTo': [self.checkpoints[1], self.checkpoints[2], self.checkpoints[3], self.checkpoints[5],
                       self.checkpoints[5], self.checkpoints[4], self.checkpoints[4], self.checkpoints[6],
                       self.checkpoints[6], self.checkpoints[9], self.checkpoints[8], self.checkpoints[7],
                       self.checkpoints[8], self.checkpoints[10], self.checkpoints[11], self.checkpoints[11],
                       self.checkpoints[12], self.checkpoints[12], self.checkpoints[12], self.checkpoints[13],
                       self.checkpoints[12], self.checkpoints[15], self.checkpoints[15], self.checkpoints[14],
                       self.checkpoints[15], self.checkpoints[16], self.checkpoints[15], self.checkpoints[17],
                       self.checkpoints[18], self.checkpoints[17]],

            # Define latitude of the start point
            'fromLat': [self.checkpoints[0].lat, self.checkpoints[0].lat, self.checkpoints[2].lat,
                        self.checkpoints[2].lat, self.checkpoints[3].lat, self.checkpoints[5].lat,
                        self.checkpoints[3].lat, self.checkpoints[4].lat, self.checkpoints[5].lat,
                        self.checkpoints[6].lat, self.checkpoints[6].lat, self.checkpoints[6].lat,
                        self.checkpoints[9].lat, self.checkpoints[9].lat, self.checkpoints[9].lat,
                        self.checkpoints[10].lat, self.checkpoints[8].lat, self.checkpoints[7].lat,
                        self.checkpoints[11].lat, self.checkpoints[11].lat, self.checkpoints[13].lat,
                        self.checkpoints[12].lat, self.checkpoints[13].lat, self.checkpoints[13].lat,
                        self.checkpoints[14].lat, self.checkpoints[14].lat, self.checkpoints[16].lat,
                        self.checkpoints[16].lat, self.checkpoints[16].lat, self.checkpoints[18].lat],

            # Define longitude of the start point
            'fromLn': [self.checkpoints[0].lng, self.checkpoints[0].lng, self.checkpoints[2].lng,
                       self.checkpoints[2].lng, self.checkpoints[3].lng, self.checkpoints[5].lng,
                       self.checkpoints[3].lng, self.checkpoints[4].lng, self.checkpoints[5].lng,
                       self.checkpoints[6].lng, self.checkpoints[6].lng, self.checkpoints[6].lng,
                       self.checkpoints[9].lng, self.checkpoints[9].lng, self.checkpoints[9].lng,
                       self.checkpoints[10].lng, self.checkpoints[8].lng, self.checkpoints[7].lng,
                       self.checkpoints[11].lng, self.checkpoints[11].lng, self.checkpoints[13].lng,
                       self.checkpoints[12].lng, self.checkpoints[13].lng, self.checkpoints[13].lng,
                       self.checkpoints[14].lng, self.checkpoints[14].lng, self.checkpoints[16].lng,
                       self.checkpoints[16].lng, self.checkpoints[16].lng, self.checkpoints[18].lng],

            # Define latitude of the end point
            'toLat': [self.checkpoints[1].lat, self.checkpoints[2].lat, self.checkpoints[3].lat,
                      self.checkpoints[5].lat, self.checkpoints[5].lat, self.checkpoints[4].lat,
                      self.checkpoints[4].lat, self.checkpoints[6].lat, self.checkpoints[6].lat,
                      self.checkpoints[9].lat, self.checkpoints[8].lat, self.checkpoints[7].lat,
                      self.checkpoints[8].lat, self.checkpoints[10].lat, self.checkpoints[11].lat,
                      self.checkpoints[11].lat, self.checkpoints[12].lat, self.checkpoints[12].lat,
                      self.checkpoints[12].lat, self.checkpoints[13].lat, self.checkpoints[12].lat,
                      self.checkpoints[15].lat, self.checkpoints[15].lat, self.checkpoints[14].lat,
                      self.checkpoints[15].lat, self.checkpoints[16].lat, self.checkpoints[15].lat,
                      self.checkpoints[17].lat, self.checkpoints[18].lat, self.checkpoints[17].lat],

            # Define longitude of the end point
            'toLn': [self.checkpoints[1].lng, self.checkpoints[2].lng, self.checkpoints[3].lng,
                     self.checkpoints[5].lng, self.checkpoints[5].lng, self.checkpoints[4].lng,
                     self.checkpoints[4].lng, self.checkpoints[6].lng, self.checkpoints[6].lng,
                     self.checkpoints[9].lng, self.checkpoints[8].lng, self.checkpoints[7].lng,
                     self.checkpoints[8].lng, self.checkpoints[10].lng, self.checkpoints[11].lng,
                     self.checkpoints[11].lng, self.checkpoints[12].lng, self.checkpoints[12].lng,
                     self.checkpoints[12].lng, self.checkpoints[13].lng, self.checkpoints[12].lng,
                     self.checkpoints[15].lng, self.checkpoints[15].lng, self.checkpoints[14].lng,
                     self.checkpoints[15].lng, self.checkpoints[16].lng, self.checkpoints[15].lng,
                     self.checkpoints[17].lng, self.checkpoints[18].lng, self.checkpoints[17].lng]
        })
        # Create a np.array for saving the distances between the checkpoints
        distances = np.zeros(len(df_graph))

        # Calculate the distances between the checkpoints
        for index, row in df_graph.iterrows():
            point1 = Point(row['fromLat'], row['fromLn'])
            point2 = Point(row['toLat'], row['toLn'])

            # Create a GeoDataFrame with the points
            points_df = gpd.GeoDataFrame({'geometry': [point1, point2]}, crs=self.epgs_default)
            points_df = points_df.to_crs(self.epgs_projected)

            # Calculate the distance between the points and save it in the distances array
            distances[index] = points_df.distance(points_df.shift())[1]

        # Add the distances to the DataFrame
        df_graph['distance'] = distances

        # Create a new DataFrame with the columns nodeFrom, nodeTo and distance this represents edges and distances
        df_graph_distance = df_graph[['nodeFrom', 'nodeTo', 'distance']]

        return df_graph_distance
