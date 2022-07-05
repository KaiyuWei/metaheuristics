from models.multiple_solution.evolutionary_based.tuner.tuner import Preset, Tuner
import random
import pandas as pd
from models.multiple_solution.evolutionary_based.CRO import BaseCRO
from utils.FunctionUtil import *

root_paras = {
    "problem_size": 100,
    "domain_range": [-100, 100],
    "print_train": True,
    "objective_func": C28   # original C30
}

cro_paras = {
    "epoch": 500,
    "pop_size": 300,
    "G": [0.02, 0.2],
    "GCR": 0.1,
    # tune the following parameter
    "po": 0.4,
    "Fb": 0.9,
    "Fa": 0.1,
    "Fd": 0.1,
    "Pd": 0.1,
    "k": 3
}

preset_para = {
    "po": 0.66,
    "Fb": 0.66,
    "Fa": 0.66,
    "Pd": 0.66,
    "k": 66
}

pre = Preset(preset_para, 666, 0.66)
cro = BaseCRO(root_algo_paras=root_paras, cro_paras = cro_paras)
cro._preset_train__(pre, 160, 200)






