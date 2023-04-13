#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import math
import matplotlib.pyplot as plt
ix = [1,2,3,4,5,6,7,8,9,10]                 #
tx = list(np.linspace(0,135,10))            # measurement time
Nx = [106,80,98,75,74,73,49,38,37,22]       # amount of substance at time t
y = [math.log(i) for i in Nx]               # natural logarithm of amount of substance Nx

n = ix[-1]                                  #number of measurements

#CALCULATIONS FOR LINEAR FUNCTIONS

numeratorMean = sum([tx[i]*Nx[i] for i in range(0,10)])
mean = numeratorMean/sum(tx)
#mean2 = sum()

Sumty = sum([tx[i]*y[i] for i in range(0,10)])
Sumy = sum(y)
Sumt = sum(tx)
Sumt2 = sum([i**2 for i in tx])
Sumt22 = Sumt**2

D = (n*Sumty-Sumy*Sumt)/(n*Sumt2-Sumt22)     #using the calculation on the page 33

lifetime = -1/D                              #lifetime without error calculation

print("Lifetime without errors is {}".format(round(lifetime,1)))



y2 = [4.77+D*i for i in tx]                  # linear equation for estimation


#plot of the 

plt.scatter(tx,y,label = "Data")
plt.plot(tx,y2, label = "y = 4.77+-0.0103x")
plt.grid()
plt.legend(loc="upper right")
plt.title("Linear Set")
plt.xlabel('Time')
plt.ylabel('Logarithm of Amount of Substance')
plt.show()

#CALCULATIONS FOR NON-LINEAR FUNCTIONS

denominator = 10*sum([i**2 for i in tx]) - sum(tx)**2

xSumty = sum([tx[i] * y[i] for i in range(0,10)])                             #discrete summation of time * y

alpha = (sum([i**2 for i in tx])*sum(y) - sum(tx)*xSumty) / denominator       #alpha value

beta = (10*xSumty - sum(y) * sum(tx)) / denominator                           #beta value


Beta2 = -0.00903                                                              #given values in the pdf
Alpha2 = 4.725

lifetime2 = -1/Beta2

print("Lifetime with errors is {} +-12.3 sec".format(round(lifetime2,1)))


y3 = [Alpha2+Beta2*i for i in tx]            #linear function

#graph for non-linear set

plt.scatter(tx,y,label = "Data")
plt.plot(tx,y3, label = "y = 4.725-0.00903x")
plt.grid()
plt.legend(loc="upper right")
plt.title("Non-Linear Set")
#plt.errorbar(tx, y3, xerr=12.3, fmt='.k');
plt.xlabel('Time')
plt.ylabel('Logarithm of Amount of Substance')
plt.show()



###########################
#CALCULATION OF CHI SQUARE#
###########################

A = 112.73
tau = lifetime2                                                 #lifetime but writing as tau for simplicity

#calculating chi square using the formulation on the page 36
chi2 = sum([   ((Nx[i] - A*math.exp(-tx[i]/tau))**2) / (A*math.exp(-tx[i]/tau)) for i in range(0,10)])   

print("Chi Square value is {}".format(round(chi2,2)))                               #printing the output of chi square

DOF = 8

print("The Chi Square per DOF is {}".format(round(chi2/DOF,2)))

