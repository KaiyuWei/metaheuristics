from models.multiple_solution.evolutionary_based.tuner.tuner import Preset, Tuner
import random
import pandas as pd
from models.multiple_solution.evolutionary_based.CRO import BaseCRO
from utils.FunctionUtil import *

# test
from data_analysis.read_data.read_from import excel_to_dic
from data_analysis.process_data.process_data import proc_df
import matplotlib.pyplot as plt
import os

os.chdir("/Users/kaiyuwei/Documents/graduation project/metaheuristics/collect data")
dfs = excel_to_dic ("running.xlsx", "tuning method", 10)  # dictionary containing 10 dfs from tuning_method
del dfs[8]  # 8 has an abnormal result and cannot be used

time_dfs = {}  # dictionary of time-sequence DataFrames
lst = []  # list for final average result

for k, df in dfs.items():
    time_dfs[k] = proc_df(df, 600)  # convert all Dataframes by int time sequence

for i in range(600):
    size = len(time_dfs)
    sumup = 0.0
    for k, df in time_dfs.items():
        sumup += df.iloc[i, 0]
    avg = sumup / size
    lst.append([avg, i + 1])

tuning_result = pd.DataFrame(lst, columns=['fitness', 'time'])
tuning_result.plot(x='time', y='fitness')
plt.show()
print(tuning_result)   
print("Hello, World!")