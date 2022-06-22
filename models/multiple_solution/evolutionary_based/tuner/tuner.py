"""
parameter tuning
"""
from typing import List, Dict


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


class Tuner:
    presets: List[Preset]
    # constructor
    def __init__(self, pres: List[Preset]):
        self.presets = pres

    def init_presets(self):
        for pre in self.presets:
            pre.prob = 1 / len(self.presets)
            
    def add_preset(self, new_pre: Preset):
        self.presets.append(new_pre)

    # delete preset not defined, hard to rename

    def print_out(self):
        print('Presets in tuner:\n')
        for pre in self.presets:
            print('Name: {} Probability:{}  Used:{}\n'.format(str(pre.name), str(pre.prob), str(pre.used)))
            print(pre.parameters, '\n')

    def update_prob(self, sum_data: List[List], alpha:float=0.7):
        """
        input:
        sum_data: summary data, list of list, every entry of the list is composed like:
                [name of the preset: int, 
                [[improve, run time], [improve, run time], ...]]
        
        return:
        no return value, but set the prob attributes for presets in the tuner
        """
        weight = [0.0 for _ in range(len(self.presets))]  # a list for logging weights of presets in this update
        for entry in sum_data:
            name = entry[0]
            if self.presets[name].used:  # only for used presets               
                pre_data = entry[1]  # data for each preset           
                sum_time = 0.0
                sum_delta = 0.0
                for sin_data in pre_data:
                    sum_delta += sin_data[0]  # total improvement(delta) from last updata
                    sum_time += sin_data[1]  # total time used by the preset
                weight[name] = sum_delta / sum_time   # only weight for presets that were used is calculated
        tot_weight = sum(weight)

        # protection for unselected presets
        unselec_prob = 0
        for pre in self.presets:
            unselec_prob += pre.prob if not pre.used else 0
        rem_prob = 1 - unselec_prob 

        temp_prob = [0.0 for _ in range(len(self.presets))]  # for storing the temporary values
        for pre in self.presets:
            if (pre.used):
                temp_prob[pre.name] = alpha * pre.prob + (1 - alpha) * (weight[pre.name] / tot_weight)
        tot_prob = sum(temp_prob)
        for pre in self.presets:
            if (pre.used):
                pre.prob = rem_prob * (temp_prob[pre.name] / tot_prob)   
            pre.used = False  # set all presets to unused for the next round

        
    
                
        


            

        
            


    