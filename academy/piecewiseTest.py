import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.stats import wilcoxon

func_name = "C23"
os.chdir("C:/courses/graduation thesis/code/collect data/{}".format(func_name))
# dictionary containing 11 dfs from tuning_method
DPTP = pd.read_excel("training_result_{}.xlsx".format(func_name),
                     sheet_name="tuning method", header=0, index_col=0)
lst_DPTP = DPTP.loc[:, 'fitness'].values.tolist()
DPTP_first = lst_DPTP[:(len(lst_DPTP) // 2)]
DPTP_second = lst_DPTP[(len(lst_DPTP) // 2):]

testRes = {}
lstDic = {}
plst = []
for i in (1, 4, 5, 6, 8, 9):
    alter = "two-sided"
    varName = "pre{}".format(i)
    lstName = "lst_pre{}".format(i)

    testRes[varName] = pd.read_excel("training_result_{}.xlsx".format(func_name),
                                     sheet_name="preset {}".format(i), header=0, index_col=0)
    lstDic[lstName] = testRes[varName].loc[:, 'fitness'].values.tolist()
    half_len = len(lstDic[lstName]) // 2
    preset_first = lstDic[lstName][:half_len]
    preset_second = lstDic[lstName][half_len:]

    stat1, p1 = wilcoxon(DPTP_first, preset_first,
                         zero_method='zsplit', alternative=alter, mode='auto')
    stat2, p2 = wilcoxon(DPTP_second, preset_second,
                         zero_method='zsplit', alternative=alter, mode='auto')
    plst.append([i, stat1, p1, stat2, p2])

plst_df = pd.DataFrame(plst)
plst_df.to_excel("C:/Users/kaiyu.wei/Desktop/res.xlsx")
print(plst)
