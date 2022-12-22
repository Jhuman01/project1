from numpy import *
from matplotlib.pyplot import *
import pandas as pd

df = pd.read_csv('Lattice_Points.csv')
x_array=(df['X-axis'].tolist())
y_array=(df['Y-axis'].tolist())
align_array=(df['alignment'].tolist())

d=1

for l in range(1, len(x_array)):
	for (i,j,k) in zip(x_array, y_array, align_array):
		if sqrt((x_array[l]-i)**2+(y_array[l]-j)**2)==d:
			Energy=align_array[l]*k
	
