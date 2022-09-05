import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon, ranksums, mannwhitneyu
from rankSumTest import rankSum2Side, rankSumOneSideLess

func_name = "C29"
os.chdir("C:/courses/graduation thesis/code/collect data/{}".format(func_name))
# dictionary containing 11 dfs from tuning_method
DPTP = pd.read_excel("training_result_{}.xlsx".format(func_name),
                     sheet_name="tuning method", header=0, index_col=0)
lst_DPTP = DPTP.loc[:, 'fitness'].values.tolist()

testRes = {}
lstDic = {}
plst = []
for i in (8,):
    alter = "two-sided"
    varName = "pre{}".format(i)
    lstName = "lst_pre{}".format(i)

    testRes[varName] = pd.read_excel("training_result_{}.xlsx".format(func_name),
                                     sheet_name="preset {}".format(i), header=0, index_col=0)
    lstDic[lstName] = testRes[varName].loc[:, 'fitness'].values.tolist()

    # stat, p = rankSum2Side(lst_DPTP, lstDic[lstName])
    stat, p = rankSumOneSideLess(lst_DPTP, lstDic[lstName])
    plst.append([i, stat, p])
print(plst)
