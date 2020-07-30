# Merge - code basics
# generally used for columns wise operations

import pandas as pd

ds1 = pd.DataFrame({"city":["indore","delhi","mumbai"],
                    "temp":[45,22,31]})


ds2 = pd.DataFrame({"city":["mumbai","delhi","indore"],
                    "wind":[26,55,11]})
# format of merge
# pd.merge(ds1, ds2, on = "", how = "outer", indicator = True, suffixes = ["_left", "_right"])

# merge ds1 and ds2 on the basis of city column.




# understanding the joins 
ds1 = pd.DataFrame({"city":["indore","delhi","mumbai", "dehradun"],
                    "temp":[45,22,31, 45]})


ds2 = pd.DataFrame({"city":["mumbai","delhi","bhopal"],
                    "wind":[26,55,11]})

		 # how = "inner" by default

# outer join.
# left join
# left join
# right join

# now using of suffixs
ds1 = pd.DataFrame({"city": ["new york", "chicago", "orlando", "baltimore"],
                    "temp":[21,15,45,32],
                    "humid": [30,35,33,45]})

ds2 = pd.DataFrame({"city": ["new york", "chicago", "san diego"],
                    "temp":[31,25,35],
                    "humid": [25,30,38]})

# to change suffixes.


