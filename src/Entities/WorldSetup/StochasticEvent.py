from typing import List, Optional

class StochasticEvent:
    """
    Clase para representar un evento estocástico que puede afectar la aldea.
    """

    def __init__(self, name: str, description: str, 
                 resource_changes: Optional[dict] = None,
                 population_change: Optional[int] = None,
                 probability: float = 0.1):
        """
        Args:
            name: Nombre del evento.
            description: Descripción del evento.
            resource_changes: Diccionario con cambios en los recursos (nombre del recurso: cambio).
            population_change: Cambio en la población.
            probability: Probabilidad de que ocurra el evento.
        """
        self.name = name
        self.description = description
        self.resource_changes = resource_changes or {}
        self.population_change = population_change
        self.probability = probability

    def apply_event(self, village):
        """
        Aplica el evento a la aldea.
        """
        # Modifica los recursos de la aldea
        for resource_name, change in self.resource_changes.items():
            village.modify_resource(resource_name, change)

        # Modifica la población de la aldea
        if self.population_change is not None:
            village.modify_population(self.population_change)



# Examples
# sequia = StochasticEvent(
#     name="Sequía",
#     description="Un período prolongado de sequía afecta la aldea.",
#     resource_changes={"Agua": -50},
#     population_change=-10,
#     probability=0.2
# )

# inundacion = StochasticEvent(
#     name="Inundación",
#     description="Un fuerte aguacero causa una inundación en la aldea.",
#     resource_changes={"Madera": -20, "Piedra": -10},
#     population_change=-5,
#     probability=0.15
# )
