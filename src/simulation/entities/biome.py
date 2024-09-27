class Biome:
    biome_status = {
        'vegetation': 0,
        'animals': 0,
        'water': 0,
        'trees': 0,
        'minerals': 0,
    }

    # def __init__(self):
    #     self.villages = []

    # def add_village(self, village):
    #     self.villages.append(village)

    # def remove_village(self, village):
    #     self.villages.remove(village)

    # def get_villages(self):
    #     return self.villages

    # def get_biome_status(self):
    #     return self.biome_status

    def update_biome_status(self, attribute, value):
        self.biome_status[attribute] += value