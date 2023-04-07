import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 232852966 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = p 
    p_values = x 
    b = np.quantile(p_values, alpha) 
    confidence_interval = [0.062, b] 
    return confidence_interval[1], confidence_interval[0]
