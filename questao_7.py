import numpy as np
import numpy.random as npr

def questao_7():
    array2D_8 = npr.randint(5, size=9).reshape((3,3))

    identity = np.identity(3)

    det = np.linalg.det(array2D_8)

    inversa = np.linalg.inv(array2D_8)

    corretude = np.corrcoef(array2D_8, inversa)

    print(array2D_8)
    print(identity)
    print(det)
    print(inv)
    print(corretude)