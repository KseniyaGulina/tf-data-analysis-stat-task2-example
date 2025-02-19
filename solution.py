import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 1066531890 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    x2 = np.array([i**2 for i in x])
    x2_mean = x2.mean()
    left = chi2_rv.ppf(1 - alpha / 2, df = 2 * n)
    right = chi2_rv.ppf(alpha / 2)
    return np.sqrt(n * x2_mean / left / 20), np.sqrt(n * x2_mean / right / 20)
