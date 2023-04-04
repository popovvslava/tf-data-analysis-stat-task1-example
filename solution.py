import pandas as pd
import numpy as np
import scipy as sc

chat_id = 368379249 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = x - 645
    mean_val = x.mean()
    val = np.log(mean_val**2/np.sqrt(mean_val**2+sc.stats.tstd(x)))
    return val
