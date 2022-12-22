#!/usr/bin/env python
# coding: utf-8

# In[80]:


from numpy import *
from matplotlib.pyplot import *
import random as rnd

r=1
th=pi/3

x_axis_1=[0, r, r+r*cos(th), r, 0, -r*cos(th), 0]
y_axis_1=[0, 0, r*sin(th), 2*r*sin(th), 2*r*sin(th), r*sin(th), 0]
A=[]
B=[]
for j in range(4):
    x_axis=[k+j*(r+r*cos(th)) for k in x_axis_1]
    if(j%2==1):
        y_axis=[l-(r*sin(th)) for l in y_axis_1]
    else:
        y_axis=[l for l in y_axis_1]
    for a in x_axis:
        A.append(a)
    for b in y_axis:
        B.append(b)

    for i in range(0,11):
        x_axis=x_axis
        y_axis=y_axis+2*r*sin(th)
        scatter(x_axis, y_axis, color='blue')
        plot(x_axis, y_axis, color='green')
show()
#rint(A)
#rint(B)
AA=[]
for i in range (len(A)):
    x=(A[i],B[i])
    #rint(x)
    AA.append(x)
print(AA)

for i in range (len(AA)):
    


# In[ ]:




