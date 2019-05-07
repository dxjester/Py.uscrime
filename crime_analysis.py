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

crime_data = pd.read_csv('/Users/patrickbenitez/Desktop/Georgia Tech/Codebook/Python Projects/US Crime Project/US Crime Analysis/uscrime.txt')
crime_data.head(10)
