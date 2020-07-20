# melt function
# it is used to transform or reshape data

import pandas as pd

ds = pd.read_csv("weather4.csv")
# id_vars to remain that in rows.
pd.melt(ds, id_vars = "day", var_name  = "city", value_name = "temperature")
