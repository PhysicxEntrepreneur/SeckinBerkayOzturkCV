#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
intervals = [1042,860,307,78,15,3,0,0,0,1]
events = [0,1,2,3,4,5,6,7,8,9]
lambd = sum(np.multiply(intervals, events))/sum(intervals)
import math
import matplotlib.pyplot as plt
probab = [(lambd**i)*math.exp(-lambd)/math.gamma(i + 1) for i in np.arange(0,9.05,0.05)]
probab2 = [(lambd**i)*math.exp(-lambd)/math.factorial(i) for i in np.arange(0,9.1,1)]


fig, axs = plt.subplots(2, 2)
axs[0, 0].bar(events,intervals)
axs[0, 0].set_title("Measured Values Bar Graph")
plt.grid()
axs[1, 0].bar(np.arange(0,9.1,1),probab2)
axs[1, 0].set_title("Estimated Values Bar Graph")
plt.grid()
axs[0, 1].plot(np.arange(0,9.05,0.05),probab)
axs[0, 1].set_title("Estimated Values Line Graph")
plt.grid()
axs[1, 1].plot(events,intervals,marker='o')
axs[1, 1].set_title("Measured Values Line Graph")

fig.tight_layout()
plt.suptitle('Events vs Intervals') # or plt.suptitle('Main title')
plt.show()






# In[ ]:




