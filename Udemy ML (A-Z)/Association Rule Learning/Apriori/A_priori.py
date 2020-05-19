# Apriori is used  for market basket analysis.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# importing the datasets
ds = pd.read_csv("Market_Basket_Optimisation.csv", header = None)

# we have to create a list of all rows(int string format) to implement apriori 

tran_lst = []

for i in range(7501):
    tran_lst.append([str(ds.values[i, j]) for j in range(20)])

from apyori import apriori


# min_support = 3 products * 7 days(bcoz it is data of  1 week) / 7500 == 3*7/7501 (kitne % hai puri transaction me)
# min_confidence 0.8 is the ideal, if we want some good results then reduce it to 0.7,0.6,..., 0.2.(% of buying rhs object)
# min_lift = 3 always good logical rule or we can also write between 3-9.(if min_lift = 3, then >3 values are good but <3 are bad.)
# min_length = 2 , for buy 1 get 1 free deals, or 3 for buy 2 get 1 free deal.

rule = apriori(transactions = tran_lst, min_support = 0.003,    min_confidence = 0.2, min_lift = 3,
               min_length = 2, max_length = 2)

# Visualization the Results.
res = list(rule)

def inspect(res1):
    lhs = [tuple(res[2][0][0])[0] for res in res1]
    rhs = [tuple(res[2][0][1])[0] for res in res1]
    support = [res[1] for res in res1]
    confidence = [res[2][0][2] for res in res1]
    lift = [res[2][0][3] for res in res1]
    return list(zip(lhs, rhs, support, confidence, lift))

frame = pd.DataFrame(inspect(res), columns = ["Left Hand Side","Right Hand Side","Support","Confidence","Lift"])

frame = frame.nlargest(n = 9, columns = "Lift")

frame.to_csv("MBA_Res.csv", index = False)