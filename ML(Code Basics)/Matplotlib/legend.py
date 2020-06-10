# legend and grid function and labels.
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6]

max_t = [45, 43, 50, 42 ,42, 43]
min_t = [25, 30, 26, 28, 29, 32]
avg_t = [35, 36, 45, 40, 30, 38]

plt.title("Days Vs Temp")
plt.xlabel("Days.")
plt.ylabel("Temperature.")

plt.plot(days, max_t, label = 'Max')
plt.plot(days, min_t, label = 'Min')
plt.plot(days, avg_t, label = 'Avg')

plt.grid() # this can be important

plt.legend(loc = 'best')   
# loc can be modified to: 'best'    0	
#'upper right'	    1
#'upper left'	    2
#'lower left'	    3 
#'lower right'	    4
#'right'	        5
#'center left'	    6 
#'center right'	    7
#'lower center'	    8 
#'upper center'	    9
#'center'           10