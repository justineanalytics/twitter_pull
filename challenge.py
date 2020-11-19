import numpy as np
import pandas as pd
import statsmodels.api as sm
import csv

with open ('challenge.csv') as csvfile:
	reader = csv.dictreader(csvfile)
	for row in reader: 
		print(row['customerID'])
		