import pandas as pd
import os
from openpyxl import Workbook

def save_to_excel(df, file_name, i):
    exists = os.path.isfile(file_name)
    if not exists:
        wb = Workbook()
        wb.save(file_name)

    with pd.ExcelWriter(file_name, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
        df.to_excel(writer, sheet_name='tuning_method', startcol=(4 * i))