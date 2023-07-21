# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:46:16 2023

@author: Ari
"""

#imports
import pandas as pd
import numpy as np


#variables
h = -6
k = 0
l = 3
x = np.linspace(0, 1, 401)
wavelength = float(input("What is the wavelength of the XRD measurement in" 
                         " angstroms? "))
aluminium_concentration = np.zeros(1)
result = np.zeros(401)


# retrieving data from csv file
# INPUT DATA FILE NAME IN LINE BELOW
df = pd.read_csv("GSW3_1XRD.csv").values


third_peak_data = np.zeros(shape=(len(df),2))
                 
# filtering (-603) peak from data          
shape = np.shape(df)
for i in range(shape[0]):
    if df[i, 0] >= 55 and df[i, 0] <= 65:
        third_peak_data[i, :] = df[i, :]

# finding index of element with highest intensity reading    
max_index = np.unravel_index(np.argmax(third_peak_data, axis=None), 
                             third_peak_data.shape)

# defining angle reading related to maximum intensity measurement
theta = np.deg2rad(third_peak_data[max_index[0],0])

# defining interplanar spacing of sample
interplanar_spacing = (wavelength) / (2*np.sin(theta/2))

# looping potential concentration values until they fall within a tolerance range
for i in range(len(x)):
    y = x[i]
    a = 12.21 - 0.42*y
    b = 3.04 - 0.13*y
    c = 5.81 - 0.17*y
    beta = np.deg2rad(103.87 + 0.31*y)
    result[i] = (h**2 / ((a**2)*((np.sin(beta))**2))) + (k**2 / b**2) + (l**2 / ((c**2) * ((np.sin(beta))**2))) - ((2 * h * l * np.cos(beta)) / (a * c * ((np.sin(beta))**2))) 
    goal = 1 / (interplanar_spacing**2)
    if goal < result[0]:
        print("The concentration of aluminium in this sample is 0%.")
        break
    if abs(result[i] - goal) <= 0.00005:
        aluminium_concentration = np.append(aluminium_concentration, y)

    
if goal > result[0]:
    average_concentration = (np.sum(aluminium_concentration) / (len(aluminium_concentration) - 1)) *100
    print("The concentration of aluminium in this sample is approximately "
          "{}%" .format(average_concentration))     

