import numpy
import numpy.random as npr

def questao_1(size=8):
    a1D_1 = npr.randint(100, size=size)
    a1D_2 = npr.randint(100, size=size)
    a1D_3 = a1D_1 + a1D_2 
    return a1D_3