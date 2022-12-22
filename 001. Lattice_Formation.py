#!/usr/bin/env python
# coding: utf-8

# In[80]:


from numpy import *
from matplotlib.pyplot import *
import random as rnd
import pandas as pd

r=1
th=pi/3

x_axis_1=[0, r, r+r*cos(th), r, 0, -r*cos(th)]
y_axis_1=[0, 0, r*sin(th), 2*r*sin(th), 2*r*sin(th), r*sin(th)]
A=[]
B=[]
for j in range(11):
    x_axis=[k+j*(r+r*cos(th)) for k in x_axis_1]
    if(j%2==1):
        y_axis=[l-(r*sin(th)) for l in y_axis_1]
    else:
        y_axis=[l for l in y_axis_1]
    

    for i in range(0,11):
        x_axis=x_axis
        y_axis=y_axis+2*r*sin(th)
        #scatter(x_axis, y_axis, color='blue')
        #plot(x_axis, y_axis, color='green')
        
        for b in y_axis:
           B.append(b)
        for a in x_axis:
           A.append(a)
        
        
xlim(2.5,12.5)
ylim(5,15)

x_new_array=[]
y_new_array=[]
random_array=[]
for (i,j) in zip(A,B):
	if (i>2.5) and (i<12.5):
		if (j>5) and (j<15):
			x_new_array.append(i)
			y_new_array.append(j)
			a=rnd.random()
			random_array.append(a)
			#print(i,j)
			
scatter(x_new_array, y_new_array)
savefig('Lattice_1.png')
data=column_stack((x_new_array, y_new_array, random_array))
savetxt('Hexagonal_lattice_points.txt', data, fmt='%s')

dict = {'X_axis': x_new_array, 'Y_axis': y_new_array, 'alignment': random_array}
df = pd.DataFrame(dict)   
# saving the dataframe 
df.to_csv('Lattice_Points.csv')


