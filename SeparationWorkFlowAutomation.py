# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:00:39 2022

@author: daksh.sahni
"""

import pandas as pd
import numpy as np

##Call the data
input ="C:/Work/FNF/Workflow/Separation Workflow Report_11JAN2022.xlsx"
output ="C:/Work/FNF/Workflow/Separation Workflow Report_11JAN2022_output.xlsx"
#Create dataframe
df = pd.read_excel(input)

#Understanding the data
print(df.shape)
df.info()

#Transforming data
##Changing data type

#df['Date of Resignation'] = pd.to_datetime(df['Date of Resignation'])
#df['Configured Task Trigger Date'] = pd.to_datetime(df['Configured Task Trigger Date'])
#df['Actual Task Trigger Date'] = pd.to_datetime(df['Actual Task Trigger Date'])
#df['Task Completion Date'] = pd.to_datetime(df['Task Completion Date'])
#df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

###Creating Unique
df['unique'] = df['Employee ID'].astype(str)+"."+df['Task Name']+"."+df['Task Status']
df['unique2'] = df['Employee ID'].astype(str)+"."+df['Task Name']

## Sorting data in desc by Task Completion Date
df.sort_values(by=['unique','Task Completion Date'],inplace=True, ascending=[True,False])

#Dropping Duplicates when both are completed or both are pending and keep the first record only
df.drop_duplicates(subset=['unique'],keep='first',inplace=True)

#Dropping Duplicates when one is completed and one is pending
df.sort_values(by=['unique2','Task Status'],inplace=True, ascending=[True,True])
df.drop_duplicates(subset=['unique2'],keep='first',inplace=True)

#Drop Unique
df.drop(columns=['unique','unique2'],axis=1,inplace=True)

###exporting data
df.to_excel(output)
