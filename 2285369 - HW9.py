#!/usr/bin/env python
# coding: utf-8

# In[30]:


import random
import matplotlib.pyplot as plt
import math
import numpy as np

e = math.exp(1)                                        # Euler's number for simplicity
c1 = 2 / (1 - e**-2)                                   # Defining the constant in front of pdf for simplicity
r = [i * 10**-2 for i in range(0,100)]                 # range of numbers between 0&1
y = [-math.log(1 - (2 * i / c1 )  ) / 2 for i in r]    # pdf


listy = []                                             #
for i in range(10000):                                 #
    listy.append(random.choice(y))                     # Creating a number list of numbers from pdf (y)
    
z = y[::-1]                                            # Equivalent of not transformed pdf

### PLOTTING THE PLOT ###

weights = np.ones_like(listy)/float(len(listy)) * 5    # Normalizing the histogram to 1
plt.hist(listy, weights=weights, label = "Histogram")  # Plotting random number list histogram which is normalized to 1  
plt.plot(z,r, label = "PDF A")               # Pdf plot
plt.xlabel("Choosen Value")                            # labeling the axes
plt.ylabel("Number of Occurences")
plt.title(" The Value vs Normalized Occurences for PDFa")
plt.legend()
plt.grid()
plt.show()



### CALCULATIONS FOR PDF B ###
a = [i * 10**-2 for i in range(0,100)]                # Values of x between 0 & 1
b = [math.sqrt(i/3) for i in a]                       # Values of pdf for 0<x<1

listb = []                                            # Generation of list of randomly chosen values from the pdf
for i in range(10000):
    listb.append(random.choice(b))

    
### PLOTTING THE PLOT ###
weights2 = np.ones_like(listb)/float(len(listb)) * 5    # Normalizing the histogram to 1
plt.hist(listb, weights=weights2, label = "Histogram")  # plot of histogram
plt.plot(b,a, label = "PDF B")                          # plot of the pdf
plt.xlabel("Choosen Value")                             # labeling the axes
plt.ylabel("Number of Occurences")                      #
plt.title(" The Value vs Normalized Occurences for PDFb")
plt.legend()
plt.grid()
plt.show()


# In[ ]:




