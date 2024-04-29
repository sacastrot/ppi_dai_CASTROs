# Import standard library modules

# Import third party modules
# Import numpy library for checkpoints operations
import numpy as np

# Import local modules


class Checkpoint:
    """
    Represents a checkpoint of company ValleyRoute, with its identifier, name, latitude and longitude.

    Attributes:
    - id (int): The unique identifier number for the checkpoint.
    - name (str): The name of the checkpoint.
    - lat (float): The latitude coordinate of the checkpoint.
    - lng (float): The longitude coordinate of the checkpoint.
    """

    def __init__(self, id_checkpoint: int, name: str, lat: float, lng: float):
        """
        Initializes a new instance of the Checkpoint class.

        Args:
        - id_checkpoint (int): The unique identifier number for the checkpoint.
        - name (str): The name of the checkpoint.
        - lat (float): The latitude coordinate of the checkpoint.
        - lng (float): The longitude coordinate of the checkpoint.
        """

        self.id = id_checkpoint
        self.name = name
        self.lat = lat
        self.lng = lng

    @staticmethod
    def create_nodes() -> np.array:
        checkpoint0 = Checkpoint(0, "La Estrella", 6.1599234, -75.6376913)
        checkpoint1 = Checkpoint(1, 'Sabaneta', 6.1531035, -75.6167576)
        checkpoint2 = Checkpoint(2, 'Itagui', 6.1700374, -75.6183442)
        checkpoint3 = Checkpoint(3, 'Polideportivo Envigado', 6.1630497, -75.5968338)
        checkpoint4 = Checkpoint(4, 'Envigado', 6.1684628, -75.5846479)
        checkpoint5 = Checkpoint(5, 'Itagui Sur', 6.1886324, -75.6026334)
        checkpoint6 = Checkpoint(6, 'Poblado', 6.2024487, -75.5745657)
        checkpoint7 = Checkpoint(7, 'La Milagrosa', 6.2369277, -75.5519432)
        checkpoint8 = Checkpoint(8, 'Medellin Centro', 6.2456915, -75.5782263)
        checkpoint9 = Checkpoint(9, 'Laureles', 6.2379977, -75.5986600)
        checkpoint10 = Checkpoint(10, 'Divino Niño', 6.2591130, -75.6218592)
        checkpoint11 = Checkpoint(11, 'El Diamente', 6.2854838, -75.5866328)
        checkpoint12 = Checkpoint(12, 'Aranjuez', 6.2752501, -75.5590806)
        checkpoint13 = Checkpoint(13, 'Pedregal', 6.3011736, -75.5750302)
        checkpoint14 = Checkpoint(14, 'Bello', 6.3364196, -75.5604546)
        checkpoint15 = Checkpoint(15, 'La Camila', 6.3328052, -75.5429982)
        checkpoint16 = Checkpoint(16, 'Copacabana', 6.3502126, -75.5117512)
        checkpoint17 = Checkpoint(17, 'Comfama Copacabana', 6.3775514, -75.4831091)
        checkpoint18 = Checkpoint(18, 'Girardota', 6.3766278, -75.4469395)

        checkpoints = np.array([checkpoint0, checkpoint1, checkpoint2, checkpoint3, checkpoint4, checkpoint5,
                                checkpoint6, checkpoint7, checkpoint8, checkpoint9, checkpoint10, checkpoint11,
                                checkpoint12, checkpoint13, checkpoint14, checkpoint15, checkpoint16, checkpoint17,
                                checkpoint18])

        return checkpoints

    def __str__(self):
        """
        Returns the string representation of the Checkpoint instance.

        Returns:
        - str: The string representation of the Checkpoint instance.
        """

        return str(self.id)
