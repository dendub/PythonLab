import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg
def first():
    M = np.array([[2.,3.], [5.,4.], [0.,5.]])
    B = np.array([4.,23.,18.])
    #print(np.linalg.solve(M,B))
    print(np.linalg.matrix_rank(M))
    print(np.linalg.cond(M))
    print(scipy.linalg.lu(M))
    x = np.arange(-4,10,1)
    y = (4-2*x)/3
    z = (23-5*x)/4
    j = 18/5 + 0 *x
    plt.plot(x,y)
    plt.plot(x,z)
    plt.plot(x,j)
    a = np.linalg.lstsq(M,B, rcond=-1)
    print(a)
    plt.show()
   # Z1 = 4 - 2*x - 3*y
   # Z2 = 23 - 5*x - 4*y
   # plt.plot(x,y,Z1)
   # plt.plot(x,y,Z2)
   # plt.show()
first()
