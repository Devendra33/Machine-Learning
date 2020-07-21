import pandas as pd

ds = pd.read_csv("wheather.csv")

# now applying the groupby method
obj = ds.groupby("city") 

for city, group in obj:
    print(city)
    print(group)
    
# for selecting a perticular city domain
obj.get_group("mumbai")

obj.get_group("mumbai").describe()   # gives all details of mumbai  city

obj.max()    # gives the maximum value of cities
obj.min()    # gives the minimum value of cities
obj.mean()   # gives  the averag

obj.describe()  # gives all the details of all the cities.

obj.plot()  # it will plot chart for each cities.