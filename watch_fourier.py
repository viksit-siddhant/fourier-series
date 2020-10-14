import pickle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation,style
import math
import cmath

list_of_cn = []
lower_coeff = -50
upper_coeff = 50

with open('cn_square.pkl','rb') as f:
    list_of_cn = pickle.load(f)
num_coeffs = len(list_of_cn)

if num_coeffs != upper_coeff-lower_coeff:
    raise ValueError("Range of coefficients set isn't consistent with table of coefficients")
    
style.use('ggplot')
fig = plt.figure()
ax = plt.axes(xlim=(-2,2), ylim=(-2,2))

vectors = []

for i in range(num_coeffs+1):
    line, = ax.plot([], [])
    vectors.append(line)

path, = ax.plot([],[])

vectors.append(path)
class Square:
    def __init__(self):
        self.mem_x = []
        self.mem_y = []
    
    def f(self,t):
        results = []
        for i,j in enumerate(range(lower_coeff,upper_coeff)):
            results.append(list_of_cn[i]*cmath.exp(2*math.pi*1j*j*t))
        return results

    def clear_mem(self):
        self.mem_x = []
        self.mem_y = []

square = Square()

def init():
    path.set_data([], [])
    square.clear_mem()

    return path,

def animate(i):
    results = square.f(i)
    x = 0
    y = 0
    for i in range(num_coeffs+1):
        prev_x = x
        prev_y = y
        x += results[i].real
        y += results[i].imag
        vectors[i].set_data([prev_x,x],[prev_y,y])
    square.mem_x.append(x)
    square.mem_y.append(y)
    path.set_data(square.mem_x,square.mem_y)
    return tuple(vectors)

def gen_x():
    #Change this to change the speed at which the line moves
    delta_x = 0.00075
    num = 0
    while num <= 1:
        yield num
        num += delta_x

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=gen_x, interval=5, blit=True)

plt.show()
