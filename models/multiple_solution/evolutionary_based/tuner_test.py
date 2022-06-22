from tuner.tuner import Preset, Tuner

pre1 = Preset({'Fa' : 0.5, 'Fb' : 0.3}, 0)
pre2 = Preset({'Fa' : 0.8, 'Fb' : 0.2}, 1)
pre3 = Preset({'Fa' : 0.72, 'Fb' : 0.43}, 2)

ls = [pre1, pre2, pre3]
tuner = Tuner(ls)
tuner.init_presets()

tuner.presets[0].used = True
tuner.presets[1].used = False
tuner.presets[2].used = True

collected_data = [[0, [[10, 2], [8, 3]]], 
                  [1, [[15, 1], [7, 3]]], 
                  [2, [[12, 3], [10, 4]]]]

tuner.print_out()

tuner.update_prob(collected_data)

tuner.print_out()
sum = tuner.presets[0].prob + tuner.presets[1].prob + tuner.presets[2].prob
print(sum)




