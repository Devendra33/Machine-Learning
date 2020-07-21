# Handling Mi99ssing values of file
import pandas as pd
import numpy as np

ds = pd.read_csv("Data.csv")
# fillna()

ds.fillna(0)  # fill nan values with zero in all columns
ds.fillna({"Age": 0,
           "Salary":"not known" })  # to fill missing values accoriding to columns
ds.fillna(method  = "ffill", limit = 1)    # forward fill, copy only 1 time
ds.fillna(method = "bfill", limit = 2)     # backword fill, copy 2 times

# to fill nan with intermeadiate value of adjacent upper and lower cell 
ds.interpolate(method = "time")

# dropna()

ds.dropna()   # default how = any, drops every row which has nan value in any column
ds.dropna(how = "all")    # drops a rows when all columns are nan only

# Now thresh param, drop a row with valid(not null) numbers of values
# if thresh = 1, then atleast one not value should be present
ds.dropna(thresh = 3) # does not drop any.
ds.dropna(thresh = 4) # means requires 4 valid values, so drop rows with null value 

# Handling missing values using replace function.

dic = {"Temperature": [-32,-99999,28,-99999,32,31,34], "Windspeed": [6,7,-99999,8,-88888,2,8], "Event":["rain","sunny","no event","rain","no event","sunny","sunny"]}
df = pd.DataFrame(dic)

df.replace(-99999, np.nan)  # replaces all -99999 by Nan in whole df
df.replace([-99999, -88888], np.nan) # used for replacing multiple values

df.replace({"Temperature" : -99999,   # for replacing values according to the columns.
            "Windspeed" : -88888,   # for changing -99999 we can pass list of values as well
            "Event" : "no event"
        }, np.nan)

df.replace({-99999:np.nan,    # when just simply wants to replace this values from whole table 
            -88888:np.nan, 
            "no event": "snow"})

dic1 = {"Temperature": ["-32 f",-99999,28,-99999,"32 f",31,34], "Windspeed": ["6 mph",7,-99999 ,"8 mph",-88888,2,8], "Event":["rain","sunny","no event","rain","no event","sunny","sunny"]}
df1 = pd.DataFrame(dic1)

# tough task .....using regex
df1.replace("[A-Za-z]", "", regex = True) # replace all alphabetss with blancks

df1.replace({"Temperature": "[A-Za-z]",   # replace all alphabetss with blancks according to a columns
             "Windspeed": "[A-Za-z]"}, "", regex = True)

# Now replacing a list by list
dic2 = {"score": ["good", "poor", "excellent", "average", "good", "good","poor"], "names":["dex","aman","aru","kabir","ragju","ran","sxx"]}
df2 = pd.DataFrame(dic2)

df2.replace(["good", "poor", "excellent", "average"], [2,0,4,3])


