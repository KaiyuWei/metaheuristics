import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/kaiyuwei/Documents/graduation project/metaheuristics/collect data")

plt.rcParams['font.size'] = '15'
avData = pd.read_excel('probabilities.xlsx')
avData = avData.drop(9)
axes = avData.plot(y='Preset0')
for i in range(1, 10):
    avData.plot(ax=axes, y='Preset{}'.format(i))

plt.grid()
plt.xlabel('update times')
plt.ylabel('probability')
plt.legend(loc='lower left')
plt.show()
