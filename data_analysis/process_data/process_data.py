import pandas as pd

def proc_df(df, time):
    """
    df: DataFrame
    time: int, seconds of running, rows of the final returned DataFrame
    this function generates imported running results Dataframe and generate time-sequence dataframe.
    """
    nrow = df.shape[0]
    ncol = df.shape[1]

    lst = []
    start = 0
    pre = 0  # the previous row index of cur
    if df.iloc[pre, 1] >= 1.0:
        lst.append([df.iloc[pre, 0], 1.0])
        start = 1
    cur = 1  # mark for current row in the df
    fitness = df.iloc[cur, 0]
    for i in range(start, time):
        point = i + 1  # the time point (second) we are looking for in the df       
        while df.iloc[cur, 1] < point:   # if the time point in the df is less than the one we are looking for
            pre += 1
            cur += 1
        if df.iloc[cur, 1] >= point + 1:
            fitness = df.iloc[pre, 0]
        else:
            fitness = df.iloc[cur, 0]
        # append result to the list
        lst.append([fitness, point])

    df = pd.DataFrame(lst, columns=['fitness', 'time'])
    return df


