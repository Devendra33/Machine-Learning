# -*- coding: utf-8 -*-
"""2_daterange.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1En9EHt5KPWp-ZlT01sXMIoES_b9oXw1E
"""

# importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds = pd.read_csv("aapl_no_dates.csv")
ds.shape

# creating a date range from 6-1-2020 to 6-30-2020 for business days

# set the index of csv file.

# Now to add missing days(eg working days)
     # pad will just copy the the value of upper column

# ploting the graph

# to find the average of stock prices

# to find the average stock price ( 1st WEEK ONLY!)

# To get the hourly data



# when we know the start date but does not know the end date

# Now making a dummy dataset for produced days