from models.multiple_solution.evolutionary_based.tuner.tuner import Preset, Tuner
import random
import pandas as pd
from models.multiple_solution.evolutionary_based.CRO import BaseCRO
from utils.FunctionUtil import *

# test
from data_analysis.read_data.read_from import excel_to_dic
from data_analysis.process_data.process_data import proc_df
import os

os.chdir("/Users/kaiyuwei/Documents/graduation project/metaheuristics/collect data")

i = 4
f_name = "preset {} training.xlsx".format(i)
s_name = "preset {}".format(i)
predfs = excel_to_dic(f_name, s_name, 10)

print("Hello, World!")





