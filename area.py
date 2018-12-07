from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
import random

POINTS_NUM=1000
RADIUS=4

def base_line(x):
    return 0

def f_line(x):
    return x/2

def f_circle(x):
    #0<x<R
    return RADIUS - np.sqrt(RADIUS*RADIUS - (RADIUS-x)*(RADIUS-x))

def findIntersection(fun1, fun2, x0):
    return fsolve(lambda x: fun1(x) - fun2(x), x0)

def in_target_area(x,y):
    if(x< ist_x):
        if(y<f_line(x)):
            return True;
    else:
        if(y<f_circle(x)):
            return True;

def get_area(points):
    count=0
    for i in range(0,points):
        x=random.uniform(0,RADIUS);
        y=random.uniform(0,RADIUS);
        if(in_target_area(x,y)):
            count+=1
    return (count/points) * RADIUS*RADIUS

fig, ax = plt.subplots()

result = findIntersection(f_line, f_circle,0.0)
ist_x=result[0]

x=np.linspace(0,2*RADIUS,500)
fx1=np.linspace(0,ist_x)
fx2=np.linspace(ist_x,RADIUS)

ax.fill_between(fx1,f_line(fx1),color='green',alpha=0.5,linestyle='dashed')
ax.fill_between(fx2,f_circle(fx2),facecolor='green',linestyle='dashed',alpha=0.5)
#ax.plot(x,f_line(x),x,f_circle(x),ist_x,f_line(ist_x),'ro')
ax.plot(x,f_circle(x),label=r'$y = 4 - \sqrt{4^{2}-(4-x)^{2}}$')
ax.plot(x,f_line(x),label=r'$y=\frac{1}{2}x$')
ax.plot(ist_x,f_line(ist_x),'ro')
ax.legend()
ax.text(ist_x+0.1,f_line(ist_x),"({0:f},{1:f})".format(ist_x,f_line(ist_x)))

s= get_area(POINTS_NUM)
ax.set_title("Monte Carlo method, n={0:d}, area={1:f}".format(POINTS_NUM,s))

#ax.grid()
#plt.title(r'$\alpha > \beta$')
plt.show()
