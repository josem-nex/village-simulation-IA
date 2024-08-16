from Entities.Village import Village
from Entities.Villager import Villager
from Entities.WorldSetup import Climate, Terrain, StochasticEvent
from Knowledge.Work import Work


"""
Todas las tareas son las mismas para cada aldeano, lo que en dependencia de sus habilidades,
herramientas, recursos y estado en el momento actual se le asignará una tarea u otra.
"""
class Knowledge:
    """
    Representará las diferentes tareas que puede realizar un aldeano con orden de prioridades
    El orden de prioridades se representará por la pirámide de Maslow
    """
    def __init__(self, villager: Villager) -> None:
        self.villager = villager
        self.works_basics = []
        self.works_security = []
        self.works_social = []
        self.works_esteem = []
        self.create_basics_works()
        
        
    def add_basic_work(self, work: Work) -> None:
        self.works_basics.append(work)
    
    def add_security_work(self, work: Work) -> None:
        self.works_security.append(work)
    
    def add_social_work(self, work: Work) -> None:
        self.works_social.append(work)
    
    def add_esteem_work(self, work: Work) -> None:
        self.works_esteem.append(work)
    
    def get_work(self, village: Village, villager:Villager) -> Work:
        """
        Devuelve la tarea que el aldeano debe realizar
        """
        # Verificar las tareas básicas
        for work in self.works_basics:
            if work.can_be_done(villager, village):
                return work
        
        # Verificar las tareas de seguridad
        for work in self.works_security:
            if work.can_be_done(villager, village):
                return work
        
        # Verificar las tareas sociales
        for work in self.works_social:
            if work.can_be_done(villager, village):
                return work
        
        # Verificar las tareas de estima
        for work in self.works_esteem:
            if work.can_be_done(villager, village):
                return work
        
        return Work("Descansar", "El aldeano descansa", 0, 1)
    
    def create_basics_works(self) -> None:
        """
        Crea las tareas básicas para un aldeano
        """
        comer = Work("Comer", "El aldeano come", 1, 1)
        comer.add_required_condition(lambda villager, village: villager.hunger > 0.5)
        comer.add_required_resource("food", 1)
        self.add_basic_work(comer)
        dormir = Work("Dormir", "El aldeano duerme", 1, 1)
        dormir.add_required_condition(lambda villager, village: villager.energy < 0.3)
        self.add_basic_work(dormir)
        recolectar = Work("Recolectar", "El aldeano recolecta recursos", 1, 1)
        recolectar.add_required_condition(lambda villager, village: village.terrain.get_resource_amount("food") > 0)
        recolectar.add_required_resource("food", 1)
        self.add_basic_work(recolectar)
    