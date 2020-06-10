# ploting a barchart 
import matplotlib.pyplot as plt
import numpy as np

company = ["ggl", "amz", "ms", "fb"]
rev = [90, 136, 89, 27]

xpos = np.arange(len(company))

plt.xticks(xpos, company)
plt.title("Company Revenue")
plt.bar(xpos, rev)

# now making 2 bars in one area
profit = [45, 25, 50, 10]

plt.xticks(xpos, company)
plt.title("Company Revenue")
plt.bar(xpos - 0.2, rev, width = 0.4, label = "revenue")
plt.bar(xpos + 0.2, profit, width = 0.4, label = "profit")
plt.xlabel("Company Name")
plt.ylabel("rev and profit")
plt.legend(shadow = True, fontsize = "large")


# for ploting a horizontal bar graph
plt.yticks(xpos, company)
plt.title("Company Revenue")
plt.barh(xpos - 0.2, rev,)
plt.barh(xpos + 0.2, profit,)
