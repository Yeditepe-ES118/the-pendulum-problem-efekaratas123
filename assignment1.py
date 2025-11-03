import numpy as np

def find_period(L0, L1):
    g = 9.81  # m/s^2

    for L in range(L0, L1 + 1):
        T = 2 * np.pi * np.sqrt(L / g)
        print("When L = %.1f m,  T = %.1f s" % (L, T))
    
    T0 = 2 * np.pi * np.sqrt(L0 / g)
    T1 = 2 * np.pi * np.sqrt(L1 / g)

    return (T0, T1)

myresult = find_period(2, 10)
