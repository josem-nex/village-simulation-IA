from actions.village import VILLAGE_ACTIONS
from actions.villager import VILLAGER_ACTIONS

KEY_VILLAGE_ACTION = "village_action"
KEY_VILLAGER_ACTION = "villager_action"

class KnowledgeBase:
    def __init__(self):
        self._init_knowledge()

    def _init_knowledge(self):
        self._knowledge = {
            KEY_VILLAGE_ACTION: {},
            KEY_VILLAGER_ACTION: {}
        }
        
        for action in VILLAGE_ACTIONS:
            self._knowledge[KEY_VILLAGE_ACTION][action.name] = 0

        for action in VILLAGER_ACTIONS:
            self._knowledge[KEY_VILLAGER_ACTION][action.name] = 0

    def get_village_knowledge(self, key):
        return self._knowledge[KEY_VILLAGE_ACTION][key]
    
    def get_villager_knowledge(self, key):
        return self._knowledge[KEY_VILLAGER_ACTION][key]

    def update_village_knowledge(self, key, value):
        stored = self._knowledge[KEY_VILLAGE_ACTION][key]
        
        if stored == 0:
            self._knowledge[KEY_VILLAGE_ACTION][key] = value
            return        
        
        new = (stored + value) / 2
        self._knowledge[KEY_VILLAGE_ACTION][key] = new

    def update_villager_knowledge(self, key, value):
        stored = self._knowledge[KEY_VILLAGE_ACTION][key]

        if stored == 0:
            self._knowledge[KEY_VILLAGER_ACTION][key] = value
            return
        
        new = (stored + value) / 2
        self._knowledge[KEY_VILLAGER_ACTION][key] = new
