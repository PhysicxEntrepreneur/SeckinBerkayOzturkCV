#!/usr/bin/env python
# coding: utf-8

# In[2]:


Notes = ["mt1","mt2","Fin","Lab","Hw","Att"]
from pylab import scatter,xlabel,ylabel,xlim,ylim,show
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

for q in Notes:

    df = pd.read_excel (r'data13.xlsx') # the file should be in the same directory as the python script

    z = df.loc[:,q]



    mylist = []
    for i in range(100):
        if z[i] not in mylist:
            mylist.append(z[i])


    otherlist = []
    for i in range(100):
        otherlist.append(z[i])


    otherlist.sort()
    checklist = []
    counts = []
    for i in otherlist:
        if i not in checklist:
            counts.append(otherlist.count(i))
        checklist.append(i)

    mylist.sort()


    

    arr = np.array(mylist)

    newarr = np.array_split(arr, 10)



    arrcount = np.array(counts)
    newcount = np.array_split(arrcount,10)
    

    listx = [np.sum(i) for i in newcount] #eşit aralıklarda kaç birim olduğu
    
    xlabel("Notes out of 10")
    ylabel("Repetition")
    plt.bar([1,2,3,4,5,6,7,8,9,10],listx)
    plt.show()

    ##############################################################################
    #                                GAUSS FIT
    ##############################################################################


    
    mean = statistics.mean(mylist)
    sd = statistics.stdev(mylist)

    plt.xlabel('Notes')
    plt.ylabel('Distribution')
    

    # displaying the title
    plt.title(q)
    plt.plot(mylist, norm.pdf(mylist, mean, sd))
    plt.show()
    


# In[ ]:




