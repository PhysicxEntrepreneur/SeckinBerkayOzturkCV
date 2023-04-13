#!/usr/bin/env python
# coding: utf-8

# In[18]:


Notes = ["mt1","mt2","Fin","Lab","Hw","Att"]
from pylab import scatter,xlabel,ylabel,xlim,ylim,show
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
import math
NotesMatrix = []

for q in Notes:

    df = pd.read_excel (r'data13.xlsx') # the file should be in the same directory as the python script

    z = df.loc[:,q]
    
    NotesMatrix.append(z)
MeanMatrix = []
StDevMatrix = []
MedianMatrix = []
SkewnessMatrix = []
for i in range(6):
    MeanMatrix.append(sum(NotesMatrix[i])/len(NotesMatrix[i]))
    CumDeviation = 0
    for x in NotesMatrix[i]:
        CumDeviation += (MeanMatrix[i] - x)**2
    StDevMatrix.append(math.sqrt(CumDeviation/len(NotesMatrix[i])))
    
for i in range(6):
    sq = np.array(NotesMatrix[i])
    sq.sort()
    MedianMatrix.append(sq[50])

for i in range(6):
    for x in NotesMatrix[i]:
        CumDeviation += (-MeanMatrix[i] + x)**3
    if CumDeviation > 0:
        SkewnessMatrix.append("+")
    elif CumDeviation < 0:
        SkewnessMatrix.append("-")
    elif CumDeviation == 0:
        SkewnessMatrix.append("0")

        

        
dataTable = {'Name': Notes, 'Mean': MeanMatrix ,'Median' : MedianMatrix, 'Standard Deviation' : StDevMatrix , 'Direction of The Skew' : SkewnessMatrix  }
dfTable = pd.DataFrame(dataTable)
display(dfTable)


# In[2]:





# In[17]:





# In[ ]:




