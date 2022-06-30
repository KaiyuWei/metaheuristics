from typing import Dict

class Preset:
    prameters: Dict[str, float]
    prob: float
    name: int
    used: bool  # if the preset is used in after last probability update

    def __init__(self, pa: Dict[str, float], name: int, pr: float=0, used=False):
        if 0 <= pr <= 1:
            self.parameters = pa
            self.prob = pr  # probability of the preset
            self.name = name
            self.used = used
        else:
            raise Exception('probability of a Preset should be in [0, 1]')  
    
    def add_pair(self, para_name: str, value: float):
        self.parameters[para_name] = value

    def print_out(self):
        print(self.parameters)