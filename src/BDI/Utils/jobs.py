import enum

class JobStatus(enum.Enum):
    PENDING = 1
    RUNNING = 2
    COMPLETED = 3
    FAILED = 4

class Job:
    def __init__(
        self, 
        name, 
        duration, 
        status=JobStatus.PENDING,
        required_resources= None,
        reward=None,
        skill_required=None,
        risk_factor=0):
        
        self.name = name
        self.duration = duration
        self.status = status
        self.required_resources = required_resources or {}
        self.reward = reward or {}
        self.skill_required = skill_required
        self.risk_factor = risk_factor

    def __str__(self) -> str:
        return f'Job {self.name} with duration {self.duration} days, risk: {self.risk_factor}'
    def __repr__(self) -> str:
        return self.__str__()

jobs = [
    
    Job(name="Recolectar madera", duration=2, reward={'madera': 20}, skill_required='tala', risk_factor=10),
    Job(name="Recolectar agua", duration=1, reward={'agua': 20}, skill_required='recoleccion', risk_factor=5),
    
    # Agricultura
    Job(name="Cultivar trigo", duration=5, reward={'alimentos': 20}, skill_required='agricultura', risk_factor=10),
    Job(name="Sembrar semillas", duration=1, required_resources={'semillas': 10}, reward={'semillas': 10}, skill_required='agricultura', risk_factor=5),
    Job(name="Cosechar", duration=2, required_resources={'herramientas': 1}, reward={'alimentos': 30}, skill_required='agricultura', risk_factor=15),
    Job(name="Construir invernadero", duration=5, required_resources={'madera': 20, 'herramientas': 5}, reward={'alimentos': 50}, skill_required=['construccion', 'agricultura'], risk_factor=20),

    # Pesca
    Job(name="Pescar", duration=2, reward={'alimentos': 15}, skill_required='pesca', risk_factor=25),
    Job(name="Reparar red", duration=1, required_resources={'cuerda': 5}, skill_required='pesca', risk_factor=10),
    Job(name="Construir barco", duration=10, required_resources={'madera': 50, 'herramientas': 10}, reward={'pescado': 50}, skill_required=['construccion', 'pesca'], risk_factor=30),

    # Caza
    Job(name="Cazar conejos", duration=1, reward={'carne': 10}, skill_required='caza', risk_factor=35),
    Job(name="Cazar ciervos", duration=3, reward={'carne': 25}, skill_required='caza', required_resources={'arma': 1}, risk_factor=45),
    Job(name="Fabricar trampas", duration=1, required_resources={'madera': 5, 'cuerda': 2}, reward={'trampas': 5}, skill_required='caza', risk_factor=20),

    # Construcción
    Job(name="Construir cabaña", duration=5, required_resources={'madera': 50, 'piedra': 10}, reward={'refugio': 1}, skill_required='construccion', risk_factor=15),
    Job(name="Construir muro", duration=8, required_resources={'madera': 30, 'piedra': 20}, reward={'defensa': 1}, skill_required='construccion', risk_factor=25),
    Job(name="Mejorar herramientas", duration=2, required_resources={'madera': 5, 'hierro': 2}, reward={'herramientas': 5}, skill_required='herreria', risk_factor=10),

    # Minería
    Job(name="Extraer piedra", duration=3, reward={'piedra': 20}, skill_required='mineria', risk_factor=30),
    Job(name="Extraer hierro", duration=5, reward={'hierro': 10}, skill_required='mineria', required_resources={'pico': 1}, risk_factor=40),
    Job(name="Construir horno", duration=5, required_resources={'piedra': 30, 'madera': 10}, reward={'horno': 1}, skill_required='construccion', risk_factor=20),

   ]