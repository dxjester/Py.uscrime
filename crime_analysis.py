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
#----------------------------------- START -----------------------------------#
#-------------------- PHASE 1: Import & Clean the Dataset --------------------#
#-----------------------------------------------------------------------------#

# read in the file 
url = '/Users/patrickbenitez/Desktop/Georgia Tech/Codebook/Git Projects/PY.uscrime/uscrime.txt'
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

plt.boxplot(crime_df['row'])
plt.title('row: Box and Whisker')
plt.tight_layout()
plt.show()

for col in col_list:
    filename = 'Box & Whisker: ' + col + '.png'
    plt.boxplot(crime_df[col])
    plt.title(col + ': Box and Whisker')
    plt.tight_layout()
    plt.show()
    plt.savefig('Charts/Box & Whisker Plots/' + filename)
    

crime_df['row']