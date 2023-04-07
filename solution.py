import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 1066531890 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    s = np.std(x)
    alpha = 1 - p
    #left = chi2.ppf(1 - alpha/2, n-1)
    #right = chi2.ppf(alpha/2, n-1)
    left = chi2.ppf(alpha/2, n-1)
    right = chi2.ppf(1 - alpha/2, n-1)
    return np.sqrt((n-1) * s**2 / left / 20), \
           np.sqrt((n-1) * s**2 / right / 20)
