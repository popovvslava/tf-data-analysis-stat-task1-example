import pandas as pd
import numpy as np
import scipy as sc

chat_id = 368379249 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return np.log(x-643).mean()
