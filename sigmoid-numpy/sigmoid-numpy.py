import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Vectorized sigmoid function.
    """
    x_arr = np.array(x)
    result = 1/(1 + np.exp(-x_arr))

    if x_arr.ndim == 0:
        return float(result)

    return result