class Climate:
    """
    Clase para representar el clima de un terreno.
    """

    def __init__(self, name: str, temperature: int, rainfall: int):
        """
        Inicializa un objeto Climate.

        Args:
            name: Nombre del clima.
            temperature: La temperatura en la que se encuentra el Terreno.
            rainfall: La cantidad de lluvia o de sequía del Terreno.
        """
        self.name = name
        self.temperature = temperature
        self.rainfall = rainfall
