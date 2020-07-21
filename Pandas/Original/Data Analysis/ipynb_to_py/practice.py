# Handling Mi99ssing values of file
import numpy as np
import pandas as pd
# fillna()
ds = pd.read_csv("Data.csv")

# forward fill, copy only 1 time with limit parameter
# to fill nan with intermeadiate value of adjacent upper and lower cell 
# dropna()
dic = {"Temperature": [-32,-99999,28,-99999,32,31,34], "Windspeed": [6,7,-99999,8,-88888,2,8], "Event":["rain","sunny","no event","rain","no event","sunny","sunny"]}
df = pd.DataFrame(dic)
# use replace

dic1 = {"Temperature": ["-32 f",-99999,28,-99999,"32 f",31,34], "Windspeed": ["6 mph",7,-99999 ,"8 mph",-88888,2,8], "Event":["rain","sunny","no event","rain","no event","sunny","sunny"]}
df1 = pd.DataFrame(dic1)

# replace hard

# Now replacing a list by list
dic2 = {"score": ["good", "poor", "excellent", "average", "good", "good","poor"], "names":["dex","aman","aru","kabir","ragju","ran","sxx"]}
df2 = pd.DataFrame(dic2)
