import numpy as np
import numpy.random as npr



def questao_3(matriz, size=8):
    a2D_4 = npr.randint(100, size = size)
    a2D_4 = a2D_4.reshape(2, size/2)
    a2D_4 = a2D_4 * matriz
    return a2D_4
