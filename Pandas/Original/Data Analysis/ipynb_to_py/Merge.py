# Merge - code basics
# generally used for columns wise operations

import pandas as pd

ds1 = pd.DataFrame({"city":["indore","delhi","mumbai"],
                    "temp":[45,22,31]})


ds2 = pd.DataFrame({"city":["mumbai","delhi","indore"],
                    "wind":[26,55,11]})
ds = pd.merge(ds1, ds2, on = "city" )



# understanding the joins 
ds1 = pd.DataFrame({"city":["indore","delhi","mumbai", "dehradun"],
                    "temp":[45,22,31, 45]})


ds2 = pd.DataFrame({"city":["mumbai","delhi","bhopal"],
                    "wind":[26,55,11]})

ds = pd.merge(ds1, ds2) # how = "inner" by default

# outer join.
ds = pd.merge(ds1, ds2, how = "outer")

# left join
ds = pd.merge(ds1, ds2, how = "left")

# right join
ds = pd.merge(ds1, ds2, how = "right")

# now using of suffixs
ds1 = pd.DataFrame({"city": ["new york", "chicago", "orlando", "baltimore"],
                    "temp":[21,15,45,32],
                    "humid": [30,35,33,45]})

ds2 = pd.DataFrame({"city": ["new york", "chicago", "san diego"],
                    "temp":[31,25,35],
                    "humid": [25,30,38]})

ds = pd.merge(ds1, ds2,on = "city", suffixes = ["_left","_right"])