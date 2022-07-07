import pandas as pd

def excel_to_dic (f_name, s_name, nr_table):
    """
    this function read an excel file and import tables from it as dictionary of DataFrames.
    """
    df_dic = {}  # dictionary for import DataFrames
    for i in range(nr_table):  # read tables
        df_dic[i] = pd.read_excel(f_name, sheet_name=s_name, header=0, index_col=0, usecols=[i * 4 + j for j in range(3)])
    return df_dic

