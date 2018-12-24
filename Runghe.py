import math
#import matplotlib.pyplot as plt
#import numpy as np

def f(x, y):
    return (0.1*(x+(y*y)))
x = [0]
y=[1]
func=[]
hfunc=[]
err = []
h = 0.015
for i in range(19):
    x.append(x[i]+h)
    #print( str(i) + "   "+ str(x[i]))

for i in range(20):
    k1=f(x[i],y[i])
    k2=f(x[i]+(h/2),y[i]+k1*(h/2))
    k3=f(x[i]+(h/2),y[i]+k2*(h/2))
    k4=f(x[i]+ h,y[i]+h*k3)
    delta=(h/6)*(k1+2*k2+2*k3+k4)
    y.append(y[i]+delta)
    print( str(round(x[i],5))  + "  " + str(round(y[i],5))+"   ")
    #func.append(f(x[i-1],y[i-1]))
   #hfunc.append(h*f(x[i-1],y[i-1]))
