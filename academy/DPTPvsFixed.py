import random
import pandas as pd

# test
import matplotlib.pyplot as plt
import os

os.chdir("/Users/kaiyuwei/Documents/graduation project/metaheuristics/collect data")
# dictionary containing 11 dfs from tuning_method
data = {}
DPTP = pd.read_excel("training_result.xlsx",
                     sheet_name="tuning method", header=0, index_col=0)
data['DPTP'] = DPTP
for i in range(10):
    st_name = "preset {}".format(i)
    df = pd.read_excel("training_result.xlsx",
                       sheet_name=st_name, header=0, index_col=0)
    data[str(i)] = df

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
for ax in (ax1, ax2, ax3, ax4):
    data['DPTP'].plot(ax=ax, x="time", y="fitness",
                      label="DPTP(r = 30)", linestyle='dashed')

for i in range(2):
    lb = "Preset {}".format(i)
    data[str(i)].plot(ax=ax1, x="time", y="fitness", label=lb)

for i in range(2, 4):
    lb = "Preset {}".format(i)
    data[str(i)].plot(ax=ax2, x="time", y="fitness", label=lb)

for i in range(4, 7):
    lb = "Preset {}".format(i)
    data[str(i)].plot(ax=ax3, x="time", y="fitness", label=lb)

for i in range(7, 10):
    lb = "Preset {}".format(i)
    data[str(i)].plot(ax=ax4, x="time", y="fitness", label=lb)

ax_titles = {ax1: "a", ax2: "b", ax3: "c", ax4: "c"}
for ax in (ax1, ax2, ax3, ax4):
    ax.set(xlabel='time(seconds)', ylabel='fitness')
    ax.set_title(ax_titles[ax])
    ax.grid()


plt.show()
