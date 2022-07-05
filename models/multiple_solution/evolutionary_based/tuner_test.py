from tuner.tuner import Preset, Tuner
import random
import pandas as pd

random.seed(1800)
my_tuner = Tuner()
input_range = {'p1': [0.2, 0.5], 'p2': [0.22, 0.68], 'k': [4, 10]}
my_tuner.random_gen(10, input_range)
allPresets = pd.DataFrame()
for pre in my_tuner.presets:
    df = pd.DataFrame(pre.parameters, index=[pre.name])
    allPresets = allPresets.append(df)
print(allPresets)






