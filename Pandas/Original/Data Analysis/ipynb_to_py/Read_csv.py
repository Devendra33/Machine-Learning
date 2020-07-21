import pandas as pd

# Reading a file
col =  ['index', 'nbaDebutYear', 'firstName', 'lastName', 'jersey',
       'heightMeters', 'weightKilograms', 'int_dt'] 
ds = pd.read_csv("player_data.csv", header = None, names = col)  # reading  a file with column titles
ds = pd.read_csv("player_data.csv", header = 0) # can be used for skipping the rows,
                                                # header = 0, it is default
                                                # if header = 1 then first row become title

ds = pd.read_csv("player_data.csv", nrows = 1 )  # to read nunber of n number of rows

ds = pd.read_csv("player_data.csv", na_values = {"jersey":[2]} ) # it makes null value, key == column name
                                                                                    #value == to make it null
                                                                                        
# Now Writing into a file.
ds.to_csv("new_file.csv", index = False, columns =['index', 'firstName', 'lastName'], header = False)
# index = False : now default index will not be visible on the file,
# columns =['index', 'firstName', 'lastName'] :  only these columns will visile on new file,
# header = False : column title will not be visible


                                                                                        

