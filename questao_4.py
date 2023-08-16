import numpy as np
import numpy.random as npr

def questao_4():
    array1D_5 = npr.randint(10, size=10)
    array1D_6 = npr.randint(10, size=10)

    n_comon = np.intersect1d(array1D_5,array1D_6)
    n_indice_comon = array1D_5 == array1D_6

    n_not_in = np.isin(array1D_6, n_comon)

    print(n_comon)
    print(n_indice_comon)
    print(array1D_5[~n_not_in])

questao_4()
    
