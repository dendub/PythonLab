import numpy as np
import sys
import matplotlib.pyplot as plt


#a = np.array([(1,2,3,4), (3,4,5,6)])

#print(a.ndim) #dimension of an array
#print(a.itemsize) #size of every elemnt
#print(a.dtype) #type of every element
#print(a.size) #size of an array
#print(a.shape) #size of array (matrix 2X3,2X2, 4X4 ...)
#a = a.reshape(4,2) # converting array in 4X2
#print(a)
#print(a[0:,3])


def first():
    a = np.random.uniform(low=0.0, high=100.0, size=(25,) )
    max=np.amax(a)
    a[a < 50.0] = 0.0
    a[a >= max] = 200.0
    print(a)

#first()

def second():
    a=np.random.randint(low = -100, high= 100,size=(9,9))
    a=a.reshape(1,81)
    a[a % 2 == 1] = 0
    a.sort()
    print(a)

#second()


def third():
    x= np.arange(0,3*np.pi,0.01)
    y= np.sin(x)
    z= np.cos(x)
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('center')

    plt.plot(x,y)
    plt.plot(x,z)
    idx = np.argwhere(np.diff(np.sign(y - z))).flatten()
    plt.plot(x[idx], y[idx], 'o')
    plt.show()

third()