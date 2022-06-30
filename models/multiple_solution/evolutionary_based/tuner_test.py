from tuner.tuner import Preset, Tuner
import random


my_tuner = Tuner()
input_range = {'p1': [0.2, 0.5], 'p2': [0.22, 0.68], 'k': [4, 10]}
my_tuner.random_gen(10, input_range)
my_tuner.print_out()






