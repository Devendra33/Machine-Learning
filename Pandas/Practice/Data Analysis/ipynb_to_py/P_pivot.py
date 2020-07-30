# pivot function 
import pandas as pd

ds = pd.read_csv("weather.csv")

# format
# ds.pivot(index = "for x-axis", columns = "for y-axis"), we can select any attribute for  rows and columns.


# Pivot Table: it is used to summarize and aggregate data inside a dataframe.
# format: pivot_table(index = "", columns = "", aggfunc = "mean/sum/diff/prod", values = "", margins = True)
# just search numpy function on google for more operation of aggfunc.


ds = pd.read_csv("weather2.csv")


# for chi square table set margins = True


# pivot grouper

ds = pd.read_csv("weather3.csv")
# now find the avg of temp and humidity according to end of month
# set freq = "W" for according to end of week



