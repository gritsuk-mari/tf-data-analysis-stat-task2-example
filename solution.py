import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 232852966 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p 
    return (x - 0.062)/(1 - alpha) + 0.062, \ 
           (x - 0.062)/(alpha) + 0.062
