
# Creatin a pie chart using matplotlib

import matplotlib.pyplot as plt

exp_val = [1400,600,400,300,200]
exp_lab = ["Rent","Food","Phn Bill","car","other utilities"]

# normal pie chart
plt.pie(exp_val, labels = exp_lab, autopct = "%0.2f%%", radius = 1.5, shadow = True, explode = [0,0,0,0,0])

# splitted pie chart
plt.pie(exp_val, labels = exp_lab, autopct = "%0.2f%%", radius = 1.5, shadow = True, explode = [0.3,0.2,0,0,0])
 