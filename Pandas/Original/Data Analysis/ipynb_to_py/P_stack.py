
import pandas as pd
ds = pd.read_excel("stocks.xlsx", header = [0,1])
ds

 	 # changes the inner most header
	 # changes the top most header

# reverse transformation

# now with 3 header
ds = pd.read_excel("stocks_3_levels.xlsx", header = [0,1,2])
ds

  # changes inner most attributes
  # changes top most attributes
  # changes middle attributes