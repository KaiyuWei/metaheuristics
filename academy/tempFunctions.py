import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'C23': 8, 'C24': 4, 'C25': 1, 'C26': 5, 'C27': 8, 'C28': 8, 'C29': 10}
courses = list(data.keys())
values = list(data.values())
fig, ax = plt.subplots()

for i in range(2, 10, 2):
    ax.hlines(y=i, xmin=-1, xmax=8, linewidth=0.8, color='silver')

ax.hlines(y=10, xmin=-1, xmax=8, linewidth=0.8, color='r', linestyle='dashed')
# creating the bar plot
plt.bar(courses, values,
        width=0.3, color='lightseagreen')
plt.plot()
plt.xlabel("Presets")
plt.ylabel("No. of overwhelmed presets")
plt.savefig("C:/Users/kaiyu.wei/Downloads/NoOfPresets.png", dpi=150)
