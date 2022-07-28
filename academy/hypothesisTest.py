import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon

os.chdir("/Users/kaiyuwei/Documents/graduation project/metaheuristics/collect data")
# dictionary containing 11 dfs from tuning_method
DPTP = pd.read_excel("training_result.xlsx",
                     sheet_name="tuning method", header=0, index_col=0)
lst_DPTP = DPTP.loc[:, 'fitness'].values.tolist()

testRes = {}
lstDic = {}
plst = []
for i in (4,):
    alter = "two-sided"
    varName = "pre{}".format(i)
    lstName = "lst_pre{}".format(i)

    testRes[varName] = pd.read_excel("training_result.xlsx",
                                     sheet_name="preset {}".format(i), header=0, index_col=0)
    lstDic[lstName] = testRes[varName].loc[:, 'fitness'].values.tolist()

    stat, p = wilcoxon(lst_DPTP, lstDic[lstName],
                       zero_method='zsplit', alternative=alter)
    plst.append([i, stat, p])
print(plst)
