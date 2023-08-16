import numpy as np
import numpy.random as npr



def questao_5():
    array1D_5 = npr.randint(10, size=10)
    array1D_6 = npr.randint(10, size=10)

    array1D_7 = np.hstack((array1D_5, array1D_6))

    average = np.average(array1D_7)
    variancia = np.var(array1D_7)
    std = np.std(array1D_7)

    print(f"media: {average}")
    print(f"desvio padrão: {std}")
    print(f"variância: {variancia}")

    array1D_7[array1D_7 % 2 == 1] = -1
    array1D_7[array1D_7 % 2 == 0] = 1

    print(array1D_7)
    
    return array1D_7

questao_5()