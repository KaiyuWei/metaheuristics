import math
import scipy.stats as st
import os
import pandas as pd
import copy


def rankSum2Side(s1, s2):
    """
    s1: data from DPTP list
    s2: data from preset list
    """
    n = len(s1)  # sample size
    conList = copy.deepcopy(s1)

    for i in s2:
        conList.append(i)  # concatenate two lists

    rank = st.rankdata(conList)[:n]

    rankSum = sum(rank)
    expec = n * (2 * n + 1) / 2
    std = math.sqrt(n * n * (2 * n + 1) / 12)

    stat = float((rankSum - expec) / std)
    p0 = 0.0
    if stat <= 0:
        p0 = st.norm.cdf(stat)
    else:
        p0 = 1 - st.norm.cdf(stat)

    p_value = float(min(1.0, 2 * p0))

    return stat, p_value


def rankSumOneSideLess(s1, s2):
    """
    to test if s1 < s2
    """
    n = len(s1)  # sample size
    conList = copy.deepcopy(s1)

    for i in s2:
        conList.append(i)  # concatenate two lists

    rank = st.rankdata(conList)[:n]

    rankSum = sum(rank)
    expec = n * (2 * n + 1) / 2
    std = math.sqrt(n * n * (2 * n + 1) / 12)

    stat = float((rankSum - expec) / std)
    p_value = 1 - st.norm.cdf(stat)

    return stat, p_value


def rankSumOneSideLess(s1, s2):
    """
    to test if s1 < s2
    """
    n = len(s1)  # sample size
    conList = copy.deepcopy(s1)

    for i in s2:
        conList.append(i)  # concatenate two lists

    rank = st.rankdata(conList)[:n]

    rankSum = sum(rank)
    expec = n * (2 * n + 1) / 2
    std = math.sqrt(n * n * (2 * n + 1) / 12)

    stat = float((rankSum - expec) / std)
    p_value = 1 - st.norm.cdf(stat)

    return stat, p_value
