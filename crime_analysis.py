# -*- coding: utf-8 -*-
"""
FILENAME: crime_analysis.py
PROJECT: US Crime Project
DATE CREATED: 6-May-19
DATE UPDATED: 11-May-19
VERSION: 1.0
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy import stats
import seaborn as sns; sns.set() # use seaborn plotting defaults




#----------------------------------- START -----------------------------------#
#-------------------- PHASE 1: Import & Clean the Dataset --------------------#
#-----------------------------------------------------------------------------#

# read in the file 
url = '/Users/patrickbenitez/Desktop/Georgia Tech/Codebook/Python Projects/US Crime Project/US Crime Analysis/uscrime.txt'
crime_df = pd.read_csv(url, sep='\t', lineterminator='\r', header=0)
crime_df.head(10)
crime_df.dtypes # ensure attributes possess the correct data type

# retrieve administrative information of the dataframe 
df_size = crime_df.size
df_size
crime_df.shape
crime_df.ndim

# add a new 
crime_df['row'] = range(len(crime_df))
crime_df['row']

# create a list of all the column headers
col_list = crime_df.columns.tolist()
col_list


#----------------------------------- START -----------------------------------#
#-------------------- PHASE 2: Discovery & Analysis --------------------------#
#-----------------------------------------------------------------------------#

# 2.1 Box and Whisker plots of predictor attributes --------------------------#
# plot one table attribute to test matplotlib functionality
plt.boxplot(crime_df['M'])
plt.title('M: Box and Whisker')
plt.tight_layout()
plt.show()
plt.savefig('Box & Whisker: M.png')

# plot box and whisker charts for all variables minus the 'Crime' response attribute
for col in col_list:
    temp = col
    plt.boxplot(crime_df[temp])
    plt.title(col + ': Box and Whisker')
    plt.tight_layout()
    plt.savefig('Box & Whisker: ' + col +'.png')


x = crime_df.drop('Crime', axis=1)  
y = crime_df['Crime']  

# 2.2 Box and Whisker plots of predictor attributes --------------------------#
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)  