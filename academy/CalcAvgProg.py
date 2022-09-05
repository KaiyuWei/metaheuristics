import pandas as pd
import os

# for j in range(3, 9):
#     func_name = "C2{}".format(j)
#     os.chdir("C:/courses/graduation thesis/code/collect data/{}".format(func_name))

#     # read all data from sheets into one dictionary
#     prob_dic = {}
#     for i in range(5):
#         prob_dic[i] = pd.read_excel("probabilities_{}.xlsx".format(func_name),
#                                     sheet_name="probabilities exepriment {}".format(i), header=0, index_col=0)

#     rowSum = prob_dic[0].iloc[-1, :]
#     for i in range(1, 5):
#         rowSum += prob_dic[i].iloc[-1, :]

#     avgProb = rowSum / 5

#     with pd.ExcelWriter("C:/courses/graduation thesis/code/collect data/avgProbs.xlsx",
#                         engine='openpyxl', mode='a') as writer:
#         avgProb.to_excel(writer, sheet_name="prob_{}".format(func_name))

func_name = "C29"
os.chdir("C:/courses/graduation thesis/code/collect data/{}".format(func_name))

# read all data from sheets into one dictionary
prob_dic = {}
for i in range(5):
    prob_dic[i] = pd.read_excel("probabilities_{}.xlsx".format(func_name),
                                sheet_name="probabilities exepriment {}".format(i), header=0, index_col=0)

rowSum = prob_dic[0].iloc[-1, :]
for i in range(1, 5):
    rowSum += prob_dic[i].iloc[-1, :]

avgProb = rowSum / 5

with pd.ExcelWriter("C:/courses/graduation thesis/code/collect data/avgProbs.xlsx",
                    engine='openpyxl', mode='a') as writer:
    avgProb.to_excel(writer, sheet_name="prob_{}".format(func_name))
