from Entities.WorldSetup.StochasticEvent import StochasticEvent
from Entities.WorldSetup.Terrain import Terrain
from Entities.WorldSetup.Climate import Climate
from Entities.Village import Village
# Examples
if __name__ == "__main__":
    # Ejemplo de creación de una aldea
    sequia = StochasticEvent(
        name="Sequía",
        description="Un período prolongado de sequía afecta la aldea.",
        resource_changes={"Agua": -50},
        population_change=-10,
        probability=0.2
    )
    
    inundacion = StochasticEvent(
        name="Inundación",
        description="Un fuerte aguacero causa una inundación en la aldea.",
        resource_changes={"Madera": -20, "Piedra": -10},
        population_change=-5,
        probability=0.15
    )
    
    clima = Climate("Lluvioso", 25, 90)
    terrain = Terrain("Savana",None,climate=clima)
    village = Village(
        name="Willow Creek",
        terrain=terrain,
        population=[],
        resources={
            "Madera": 150,
            "Piedra": 75,
            "Agua": 120,
            "Hierro": 30
        },
        buildings=["Casa", "Granja"],
        events=[sequia, inundacion]
    )
    