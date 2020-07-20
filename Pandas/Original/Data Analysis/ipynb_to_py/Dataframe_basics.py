#Dataframe Operations
import pandas as pd

# Creating Dataframe
# from csv file
ds = pd.read_csv("File_name.csv")

# from dictionary
dic  = {"name":["alok", "dev", "aman", "akshay"], "roll":[15,34,15,12], "course":["CSE-BAO","CSE-BAO","CSE-BAO","CSE-BAO"]}
ds = pd.DataFrame(dic)

# from LIST
# from tuple in list   IMP: Each tuple in the list is ROW
l = [("ALOK", 12,"CSE-BAO"),("DEV", 34,"CSE-BAO"),("AMAN", 15,"CSE-BAO")]
ds =  pd.DataFrame(l, columns = ["Names", "Roll", "Course"])

# dictionary in list

l = [{ 'firstName': 'LaMarcus', 'lastName': 'Aldridge', 'jersey': '12', 'heightMeters': '2.11', 'nbaDebutYear': '2006', 'weightKilograms': '117.9'},
     { 'firstName': 'LeBron', 'lastName': 'James', 'jersey': '2', 'heightMeters': '2.03', 'nbaDebutYear': '2003', 'weightKilograms': '113.4' },
     { 'firstName': 'Kawhi', 'lastName': 'Leonard', 'jersey': '2', 'heightMeters': '2.01', 'nbaDebutYear': '2011', 'weightKilograms': '104.3' }]
ds = pd.DataFrame(l)

l_int = [55,96,5]  #add this to columns of ds
ds["int_dt"] = l_int
ds.columns # gives the list of columns names

# to select Rows
ds.head(3)  # default = 5, select from upper portion
ds.tail(3)  # default = 5  selects from lower portion

# MAIN FORMAT DS["ROWS"]["COLUMNS"]
ds[0:2]["lastName"] # selects 0,1 row of jersey
ds[0:2][["lastName","jersey"]]

 #for selecting rows from any where ds[:](selects all rows)
ds[1:3]   # selects 1,2 rows(indexs) only

# Mathematical operation
row, col = ds.shape  # tuple unpacking
ds.weightKilograms.min()     # minimum element
ds["weightKilograms"].max()   # maximum element
ds.int_dt.std()     # standard deviation
ds.describe()

# selection of Columns
# to select single column.
ds.lastName # does not work when there are gaps in columns names then, ds["lastName"] work always.

# to select group of columns 
ds[["firstName","lastName","jersey"]]

# SQL operation on dataframe
# selecting a single column, so store on a list.   
ds["jersey"][ds.int_dt > 5] # select jersey from tablename where int_dt == 5;
lst = list(ds["jersey"][ds.int_dt > 5])

# selection the multiple columns, so store on a dictionary.
ds[["firstName","lastName"]][ds.jersey == '2']
dic = dict(ds[["firstName","lastName"]][ds.jersey == '2']) # col names treated as keys.

# making columns as index
ds.set_index("nbaDebutYear", inplace = True)  # set the column as index
ds.loc["2006"]    # get information by element of index
ds.reset_index(inplace =True) # back to normal

# to  save the file as csv in the current directory. 
ds.to_csv("player_data.csv")