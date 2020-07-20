# concat - code basics
# 1 data table
import pandas as pd
india_weather = {"city":["mumbai", "delhi", "indore"],
                 "humidity":[50, 60, 80],
                 "temp":[25, 48, 42]}

us_weather = {"city":["new york", "berlin", "chicago"],
                 "humidity":[40, 65, 25],
                 "temp":[41, 43, 44]}

# creating tables from above dictionaries
ind_tab = pd.DataFrame(india_weather)
us_tab = pd.DataFrame(us_weather)

# format
# pd.concat([tab1, tab2], ignore_index = False, keys = None, join  = "outer" ,axis = 0)

ds = pd.concat([ind_tab, us_tab])  # not continoues index

ds = pd.concat([ind_tab, us_tab], ignore_index = True) # now it is in continous order
                                                        # we cannot use keys param with ignore_index.
                                                        
ds = pd.concat([ind_tab, us_tab], ignore_index = False, keys = ["india", "us"])


# now concating columns wise
temp_df = pd.DataFrame({"city":["mumbai", "delhi", "indore"],
                        "temp":[25,42,32]})

wind_df = pd.DataFrame({"city":["mumbai", "delhi", "indore"],
                        "wind":[50,72,55]})

ds = pd.concat([temp_df, wind_df], axis = 1)
