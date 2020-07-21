
import pandas as pd
ds = pd.read_excel("stocks.xlsx", header = [0,1])
ds

ds.stack(level = 1)  # changes the inner most header
ds.stack(level = 0)  # changes the top most header

# reverse transformation
stacked = ds.stack()
stacked.unstack()

# now with 3 header
ds = pd.read_excel("stocks_3_levels.xlsx", header = [0,1,2])
ds

ds.stack() # changes inner most attributes
ds.stack(level = 0)  # changes top most attributes
ds.stack(level = 1) # changes middle attributes