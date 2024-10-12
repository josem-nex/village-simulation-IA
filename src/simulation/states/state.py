class State:
    @property
    def state(self):
        return self._state
    @property
    def fuzzy_functions(self):
        return self._fuzzy_functions
    
    def get_attribute_value(self, attribute):
        return self._state[attribute]
    
    def get_attribute(self, attribute):
        return self.fuzzy_functions[attribute]()
    
    def get_attributes(self):
        return self.state.keys()
    
    def update_attribute(self, attribute, value):
        self._state[attribute] += value
    
    def show_state(self):
        [print(f'{attribute} : ({self.get_attribute(attribute)}, {self.get_attribute_value(attribute)})') for attribute in self.state]
