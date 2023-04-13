#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import matplotlib.pyplot as plt


N = [0,1,2,3,4,5]                             #    Measurement Data 
f = [447,132,42,21,3,2]                       #    Frequency Data

dl = [i * 10**-2 for i in range(1,1000,5)]    # Creating values for lambda iteration

#Calculation of the denominator as product of factorials of measurements
k = 1
for i in N:
    k *= math.factorial(i)

L = []
for i in dl:                                                        # Computing the likelihood according to possion distribution                             
    L.append(  math.exp(-len(N)*i) * i**(sum(N)) / k     )          #                          

    
LogL = []
for i in L:
    LogL.append(math.log(i))                                        # Converting the L values into log(L) values                                 
    
    
a = 2.5
y = [a for i in range(0,200)]
plt.plot(dl,LogL, label = "Log-Likelihood")                         # Plotting the log-likelihood vs lambda values
plt.xlabel("Lambda")                                                #  Adding x Label                                                          
plt.ylabel("Ln(L)")                                                 #  Adding y Label                                                          
plt.plot(y,LogL,linestyle = "-.", label = "Real Value")             # Showing verticle line, mean of 2.5
plt.legend(loc = "lower right")                                     #  Adding Legend               
plt.grid(linestyle = "--")                                          #  Adding grid                             
plt.title("Log-Likelihood Estimation ")                             #                                           

maxL = -11.706

plt.show()


# CALCULATION OF THE VARIANCE #

var1 = math.log(-(0.5 + maxL))                                     # Lower variance
var2 = math.log((0.5 - maxL))                                      # Upper Variance

y1 =  math.log((math.exp(-len(N)*var1) * var1**(sum(N)) / k))      # Corresponding log(L) value for the lower variant                                                                      
y2 =  math.log((math.exp(-len(N)*var2) * var2**(sum(N)) / k))      # Corresponding log(L) value for the upper variant 


plt.plot([var1,var2],[y1,y2])                                      # Plotting the graph
plt.grid()                                                         #                                                   
plt.title("Variance")                                              #                          
plt.xlabel("Lambda")                                               #                         
plt.ylabel("Log[L]")                                               #                            


# In[ ]:




