import pandas as pd
import numpy as np
import scipy as sc
https://github.com/popovvslava/tf-data-analysis-stat-task1-example/blob/main/solution.py

chat_id = 368379249 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    mean_val = x.mean()
    val = np.log(mean_val**2/np.sqrt(mean_val**2+sc.stats.tstd(x)))
    return val 
