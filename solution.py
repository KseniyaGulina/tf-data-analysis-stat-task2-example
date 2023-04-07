import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1066531890 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    s = np.std(x)
    left = chi2.ppf((1 - p)/2, n-1)
    right = chi2.ppf((1 + p)/2, n-1)
    return np.sqrt((n-1) * s**2 / left / 20), \
           np.sqrt((n-1) * s**2 / right / 20)
