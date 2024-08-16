from src.Entities.Village import Village
from src.Entities.Villager import Villager


class Work:
    """
    Representará las diferentes tareas que puede realizar un aldeano
    """
    def __init__(self, name: str, description: str, priority: int, duration: int):
        self.name = name
        self.description = description
        # priority 1: básicas, 2: seguridad, 3: sociales, 4: estima
        self.priority = priority
        self.duration = duration
        self.required_resources = {}
        self.required_buildings = []
        self.required_skills = []
        self.required_tools = []
        # ? las condiciones que se deben cumplir para realizar la tarea ?
        # por ejemplo, si es de noche no se puede trabajar
        # o para elegir la de alimentarse si tiene hambre
        self.required_conditions = []

    def add_required_resource(self, resource: str, amount: int) -> None:
        self.required_resources[resource] = amount

    def add_required_building(self, building: str) -> None:
        self.required_buildings.append(building)

    def add_required_skill(self, skill: str) -> None:
        self.required_skills.append(skill)

    def add_required_tool(self, tool: str) -> None:
        self.required_tools.append(tool)

    def add_required_condition(self, condition) -> None:
        self.required_conditions.append(condition)

    def can_be_done(self, villager: Villager, village: Village) -> bool:
        """
        Verifica si el aldeano puede realizar la tarea
        """
        # Verificar condiciones
        for condition in self.required_conditions:
            if not condition(villager, village):
                return False

        # Verificar recursos
        for resource, amount in self.required_resources.items():
            if village.resources[resource] < amount:
                return False

        # Verificar edificios
        for building in self.required_buildings:
            if building not in village.buildings:
                return False

        # Verificar habilidades
        for skill in self.required_skills:
            if skill not in villager.skills:
                return False

        # Verificar herramientas
        for tool in self.required_tools:
            if tool not in villager.tools:
                return False

        return True

    def perform_work(self, villager: Villager, village: Village) -> bool:
        """
        Realiza la tarea
        """
        # Verificar si el aldeano puede realizar la tarea
        if not self.can_be_done(villager, village):
            return False

        # Consumir recursos
        for resource, amount in self.required_resources.items():
            village.modify_resource(resource, -amount)

        # Realizar la tarea
        pass