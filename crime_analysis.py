# -*- coding: utf-8 -*-
"""
FILENAME: crime_analysis.py
PROJECT: US Crime Project
DATE CREATED: 6-May-19
DATE UPDATED: 6-May-19
VERSION: 1.0
"""


import pandas as pd
import matplotlib
import numpy as np
import csv
#----------------------------------- START -----------------------------------#
#-------------------- PHASE 1: Import & Clean the Dataset --------------------#
#-----------------------------------------------------------------------------#


infile = r'/Users/patrickbenitez/Desktop/Georgia Tech/Codebook/Python Projects/US Crime Project/US Crime Analysis/uscrime.txt'
outfile = r'/Users/patrickbenitez/Desktop/Georgia Tech/Codebook/Python Projects/US Crime Project/US Crime Analysis/uscrime.csv'

import_df = pd.read_csv(infile, sep='\t', lineterminator='\r')
import_df.head(10)

# validate data types for all attributes
import_df.dtypes

# create a copy of the clean dataframe import
master_df = import_df

# convert columns to a list 
column_list = list(master_df)
column_list

# create an empty dictionary to store five number summaries for each column
five_num_dict = {}
five_num_dict.fromkeys(["Column Header", "Min", "25% Quartile", "Mean", "75% Quartile", "Max"])
