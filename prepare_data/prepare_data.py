import pandas as pd
import os
from openpyxl import Workbook
from typing import List
from models.multiple_solution.evolutionary_based.tuner.Preset import Preset

def series_to_preset(pre):
    pre.to_dict()
   
        