import math
import scipy.stats as st
import os
import pandas as pd


def rankSum2Side(s1, s2):
    """
    s1: data from DPTP list
    s2: data from preset list
    """
    n = len(s1)  # sample size
    conList = s1

    for i in s2:
        conList.append(i)  # concatenate two lists

    rank = st.rankdata(conList)[:n]

    rankSum = sum(rank)
    expec = n * (2 * n + 1) / 2
    std = math.sqrt(n * n * (2 * n + 1) / 12)

    stat = (rankSum - expec) / std
    p_value = min(1, 1 - st.norm.cdf(stat))

    return stat, p_value
