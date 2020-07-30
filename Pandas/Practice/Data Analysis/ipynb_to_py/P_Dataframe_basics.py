#Dataframe Operations

# Creating Dataframe
# from csv file
ds = pd.read_csv("File_name.csv")

# from dictionary
dic  = {"name":["alok", "dev", "aman", "akshay"], "roll":[15,34,15,12], "course":["CSE-BAO","CSE-BAO","CSE-BAO","CSE-BAO"]}

# from LIST
# from tuple in list   IMP: Each tuple in the list is ROW
l = [("ALOK", 12,"CSE-BAO"),("DEV", 34,"CSE-BAO"),("AMAN", 15,"CSE-BAO")]


# dictionary in list

l = [{ 'firstName': 'LaMarcus', 'lastName': 'Aldridge', 'jersey': '12', 'heightMeters': '2.11', 'nbaDebutYear': '2006', 'weightKilograms': '117.9'},
     { 'firstName': 'LeBron', 'lastName': 'James', 'jersey': '2', 'heightMeters': '2.03', 'nbaDebutYear': '2003', 'weightKilograms': '113.4' },
     { 'firstName': 'Kawhi', 'lastName': 'Leonard', 'jersey': '2', 'heightMeters': '2.01', 'nbaDebutYear': '2011', 'weightKilograms': '104.3' }]


l_int = [55,96,5]  #add this to columns of ds


# to select Rows
      # default = 5, select from upper portion
      # default = 5  selects from lower portion

# MAIN FORMAT DS["ROWS"]["COLUMNS"]
         # selects 0,1 row of jersey


 #for selecting rows from any where ds[:](selects all rows)
      # selects 1,2 rows(indexs) only

# Mathematical operation
      # tuple unpacking
      # minimum element
      # maximum element
      # standard deviation
      # description of dataframe

# selection of Columns
# to select single column.
     # does not work when there are gaps in columns names then, ds["lastName"] work always.

# to select group of columns 
    

# SQL operation on dataframe
# selecting a single column, so store on a list.   
        # select jersey from tablename where int_dt == 5;
        

# selection the multiple columns, so store on a dictionary.
     # col names treated as keys.

# making columns as index
      # set the column as index
      # get information by element of index
      # back to normal

# to  save the file as csv in the current directory. 
