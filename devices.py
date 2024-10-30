# devices.py

class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.state = False  # False for OFF, True for ON

    def toggle(self):
        self.state = not self.state
        return self.state

class Light(SmartDevice):
    def __init__(self, name):
        super().__init__(name)

class Thermostat(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 20  # Default temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        return self.temperature
