import pandas as pd
import os
import matplotlib.pyplot as plt

os.chdir("/Users/kaiyuwei/Documents/graduation project/metaheuristics/collect data")
# dictionary containing 11 dfs from tuning_method
data = {}
data['DPTP'] = pd.read_excel("training_result.xlsx",
                             sheet_name="tuning method", header=0, index_col=0)
for i in range(10):
    name = str(i)
    data[name] = pd.read_excel("training_result.xlsx",
                               sheet_name="preset {}".format(i), header=0, index_col=0)

# draw the figures
axes = data['DPTP'].plot(x="time", y="fitness",
                         label="DPTP(r = 30)", linestyle='dashed')
data['7'].plot(ax=axes, x="time", y="fitness", label="Preset 7")
data['8'].plot(ax=axes, x="time", y="fitness", label="Preset 8")
data['9'].plot(ax=axes, x="time", y="fitness", label="Preset 9")
plt.grid()
plt.xlabel('time(seconds)')
plt.ylabel('fitness')
plt.show()
