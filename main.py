import numpy as np
from mpmath import *
from twin import *
from intvalpy import *
from operation import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''Код Алины из main'''
    #Interval(float('nan'), float('nan'))
    data1 = Interval(1, 10)
    data2 = Interval(1, 100)
    data3 = Interval(float('nan'), float('nan'))
    data4 = Interval(2, 6)

    T1 = Twin(data1, data2)
    print("T1 = ", T1)
    # T2 = Twin(data3, data4)
    # print("T2 = ", T2)

    # print("p(T1, T2) = ", p(T1, T2))
    # print("q(T1, T2) = ", q(T1, T2))

    # print("I1 = ", data1)
    # print("I2 = ", data2)
    # print("phi(I1, I2) = ", phi(data1, data2))
    # print("psi(I1, I2) = ", psi(data1, data2))

    # print("T1 + T2 = ", twins_plus(T1, T2))

    # print("T1 * T2 = ", twins_multiply(T1, T2))

    print("-T1 = ", unary_minus_twin(T1))

    print("1 / T1 = ", inverse_twin(T1))
