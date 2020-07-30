# Handling Mi99ssing values of file
import pandas as pd
import numpy as np

ds = pd.read_csv("Data.csv")
# fillna()

      # fill nan values with zero in all columns

              # to fill missing values accoriding to columns
              # forward fill, copy only 1 time
              # backword fill, copy 2 times

# to fill nan with intermeadiate value of adjacent upper and lower cell 


# dropna()

       # default how = any, drops every row which has nan value in any column
       # drops a rows when all columns are nan only

# Now thresh param, drop a row with valid(not null) numbers of values
# if thresh = 1, then atleast one not value should be present
         # does not drop any.
         # means requires 4 valid values, so drop rows with null value 

# Handling missing values using replace function.

dic = {"Temperature": [-32,-99999,28,-99999,32,31,34], "Windspeed": [6,7,-99999,8,-88888,2,8], "Event":["rain","sunny","no event","rain","no event","sunny","sunny"]}
# create ds of dictionary of dic and perform replace opeartions

             # replaces all -99999 by Nan in whole df
             # used for replacing multiple values

                   # for replacing values according to the columns.
                   # for changing -99999 we can pass list of values as well

            # when just simply wants to replace this values from whole table 
 

dic1 = {"Temperature": ["-32 f",-99999,28,-99999,"32 f",31,34], "Windspeed": ["6 mph",7,-99999 ,"8 mph",-88888,2,8], "Event":["rain","sunny","no event","rain","no event","sunny","sunny"]}
# create ds of dictionary of dic1 and perform regex opeartions

# tough task .....using regex
     # replace all alphabetss with blancks

           # replace all alphabetss with blancks according to a columns
    
# Now replacing a list by list
dic2 = {"score": ["good", "poor", "excellent", "average", "good", "good","poor"], "names":["dex","aman","aru","kabir","ragju","ran","sxx"]}

# create ds of dictionary of dic2 and perform replace opeartions



