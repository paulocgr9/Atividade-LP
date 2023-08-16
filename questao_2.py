import numpy as np
import numpy.random as npr
from questao_1 import questao_1

def questao_2(size=8):
    a1D_3 = questao_1()
    a2D_3_redimensionado = np.reshape(a1D_3, (2, size//2))
    a2D_3_float = a2D_3_redimensionado / 1
    a2D_3_float = float(a2D_3_redimensionado)
    return a2D_3_float

print(questao_2())