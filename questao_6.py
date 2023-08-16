import numpy as np
import numpy.random as npr

def questao_6():
    A = np.arange(4).reshape((2,2))
    B = np.arange(4).reshape((2,2))

    produto_vetorial = np.cross(A, B)

    print(produto_vetorial)

    return produto_vetorial
