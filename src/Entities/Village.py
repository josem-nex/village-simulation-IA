import random
from typing import List, Dict, Optional
from Entities.WorldSetup.StochasticEvent import StochasticEvent
from Entities.WorldSetup.Terrain import Terrain
from Entities.Villager import Villager
class Village:
    """
    Clase para representar una aldea en la simulación.
    """

    def __init__(self, name: str, terrain: Terrain, population: List[Villager], 
                 resources: Dict[str, int], buildings: List[str] = [],
                 events: List[StochasticEvent] = []):
        
        """
        Args:
            name: Nombre de la aldea.
            terrain: Terreno en el que se encuentra la aldea.
            population: Población de la aldea.
            resources: Diccionario con cantidades iniciales de recursos.
            buildings: Lista de edificios existentes en la aldea.
            events: Lista de eventos estocásticos que pueden afectar la aldea.
        """
        self.name = name
        self.terrain = terrain
        self.population = population
        self.resources = resources
        self.buildings = buildings
        self.events = events

    def modify_resource(self, resource_name: str, change: int):
        """
        Modifica la cantidad de un recurso específico.

        Args:
            resource_name: Nombre del recurso.
            change: Cambio en la cantidad del recurso.
        """
        self.resources[resource_name] += change

    def modify_population(self, change: int):
        """
        Modifica la población de la aldea.

        Args:
            change: Cambio en la población.
        """
        self.population += change

