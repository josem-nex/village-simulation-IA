from typing import Dict, Optional
from src.Entities.WorldSetup.Climate import Climate
import copy
class Terrain:
    """
    Clase base para representar un terreno en la simulación.
    """

    def __init__(self, name: str, resources: Optional[Dict[str,int]], climate: Climate,):
        """
        Args:
            name: Nombre del terreno.
            resources: Lista de tipos de recursos disponibles.
                wood
                stone
                water
                iron
                food
            climate: Clima del terreno.
        """
        self.name = name
        self.climate = climate
        if resources:
            self.resources = copy.deepcopy(resources)
        else:
            self.resources = {resource: 0 for resource in ["wood", "stone", "water", "iron", "food"]}
    def get_resource_amount(self, resource_type: str) -> int:
        """
        Devuelve la cantidad de un recurso específico.

        Args:
            resource_type: Tipo de recurso.

        Returns:
            Cantidad del recurso.
        """
        if resource_type not in ["wood", "stone", "water", "iron", "food"]:
            raise Exception("Invalid Resource")
        return self.resources[resource_type]