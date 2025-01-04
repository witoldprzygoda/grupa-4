import numpy as np
import time
from numba import jit, prange, vectorize

# Python List implementacja
def sum_of_squares_list(data):
    result = 0
    for x in data:
        result += x**2
    return result

# NumPy Array implementacja
def sum_of_squares_numpy(data):
    return np.sum(data**2)

# Numba implementacja
@jit(nopython=True)
# kod funkcji

@jit(nopython=True, fastmath=True)
# kod funkcji

@jit(nopython=True, parallel=True)
# kod funkcji

@vectorize(['int64(int64)'], target='parallel')
# kod funkcji

# testowanie
if __name__ == "__main__":
    # generowanie danych
    n = 300_000
    data_list = [i for i in range(n)]
    data_numpy = np.array(data_list, dtype=np.int64)

    # tutaj wywołanie i pomiary oraz wyniki
