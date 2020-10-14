import cmath
import math
import pickle

#f(x) can be any function defined in [0,1] -> C, which the fourier series will try to approximate
def f(x,n):
    y = math.cos(2*math.pi*x) + 2j*math.sin(2*math.pi*x)
    #Don't change this
    y *= cmath.exp(-2*math.pi*1j*n*x)
    return y

list_of_cn = []

def num_integrate(f,lower_lim=0,upper_lim=1,delta_x=0.01,n=None):
    y = lower_lim
    result = 0
    while y <= upper_lim:
        result += f(y,n)*delta_x
        y += delta_x
    return result
lower_coeff = -50
upper_coeff = 50
for i in range(lower_coeff,upper_coeff+1):
    list_of_cn.append(num_integrate(f,n=i,delta_x=0.0005))

with open('cn_square.pkl','wb') as f:
    pickle.dump(list_of_cn,f)


