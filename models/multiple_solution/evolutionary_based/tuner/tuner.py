"""
parameter tuning
"""
from pickletools import float8
from typing import List, Dict
import random
from .Preset import Preset
import numpy as np

class Tuner:
    presets: List[Preset]
    running_time: float
    cycle: int
    # constructor
    def __init__(self, pres: List[Preset]=[], cyc: int=20, running_time=600):
        self.presets = pres
        self.cycle = cyc  # the cycle length for update presets' probabilities
        self.running_time = running_time

    def init_presets(self):
        for pre in self.presets:
            pre.prob = 1 / len(self.presets)
    
    # to-do generate presets by input range

    def add_preset(self, new_pre: Preset):
        self.presets.append(new_pre)

    # delete preset not defined, hard to rename

    def print_out(self):
        print('Presets in tuner:\n')
        for pre in self.presets:
            print('Name: {} Probability:{}  Used:{}\n'.format(str(pre.name), str(pre.prob), str(pre.used)))
            print(pre.parameters, '\n')
    
    def random_gen(self, num: int, para_range: Dict[str, List]):
        """
        randomly generate presets by the range of parameters
        Only change the value of parameters that are input as auguments in this function,
        the value of other parameters will be determined by "coro_paras" in "run_CRO.py" and 
        the "RootAlgo.__init__"
        if the parameter type is int, the start and end boundaries of the input range should both be int type
        if any of the boundaries is float type, then the generated value will be float
        """
        self.presets.clear()
        for i in range(num):
            new_dict = {}
            for name in para_range:
                start = para_range[name][0]
                end = para_range[name][1]
                if isinstance(start, int) and isinstance(end, int):
                    # if both of the input boundaries are int type, use randint
                    new_dict[name] = random.randint(start, end)
                else:
                    new_dict[name] = start + (end - start) * random.random()

            new_pre = Preset(new_dict, i)
            self.presets.append(new_pre)

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

        if tot_weight:  # if only any progress has been made, otherwise probs are not changed.
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
                    if np.isnan(pre.prob):
                        raise ValueError("probability of Preset {} is NaN!".format(pre.name))
        for pre in self.presets:
            pre.used = False  # set all presets to unused for the next round
        

    def select_preset(self):
        accum = []
        bound = 0
        rand_num = random.random()  
        sel_preset: Preset
        for pre in self.presets:
            accum.append([bound, bound + pre.prob])  
            bound += pre.prob
            if accum[-1][0] <= rand_num <= accum[-1][1]:
                sel_preset = pre
                sel_preset.used = True
                return sel_preset
        raise TypeError("Preset not selected!")

            
         
     

        
    
                
        


            

        
            


    