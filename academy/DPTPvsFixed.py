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
for row in ((ax1, ax2), (ax3, ax4)):
    for axes in row:
        data['DPTP'].plot(ax=axes, x="time", y="fitness",
                          label="DPTP(r = 30)", linestyle='dashed', grid=True)

for i in range(2):
    lb = "Preset {}".format(i)
    data[str(i)].plot(ax=ax2, x="time", y="fitness", label=lb, grid=True)
ax1.set_title("a")
ax1.grid(True)

for i in range(2, 4):
    lb = "Preset {}".format(i)
    data[str(i)].plot(ax=ax3, x="time", y="fitness", label=lb, grid=True)
ax2.set_title("b")
ax2.grid(True)

for i in range(4, 6):
    lb = "Preset {}".format(i)
    data[str(i)].plot(ax=ax4, x="time", y="fitness", label=lb, grid=True)
ax3.set_title("c")
ax3.grid(True)

for i in range(6, 10):
    lb = "Preset {}".format(i)
    data[str(i)].plot(ax=ax4, x="time", y="fitness", label=lb, grid=True)
ax4.set_title("d")
ax4.grid(True)

plt.show()
