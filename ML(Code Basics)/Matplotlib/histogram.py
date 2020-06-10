# Histogram using matplotlib
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

# now creating the data.

blood_sugar_men = [80,85,85,88,90,151,100,150,121,122,135,150]
blood_sugar_women = [121,135,145,122,4,159,142,153,126,80,90,85]

plt.hist([blood_sugar_men, blood_sugar_women], bins = [80,100,120,160], label = ["men", "women"],
         rwidth = 0.9, color = ["green","yellow"])
plt.legend(shadow = True)
plt.title("Blood Sugar Analysis")
plt.xlabel("Sugar count")
plt.ylabel("Frequency of people")

