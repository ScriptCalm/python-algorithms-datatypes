# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework

import matplotlib.pyplot as plt # import Matplotlib module

# Console output requirements
print("student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework")
print() # space only
############################################################################


steps = [] # list for storing the no. of steps executed

# modified given algorithm, for demonstration purposes 
def type_number(n):
    print(n) # O(1)
    return 2 # O(1)

# loop for testing the time complexity based on different given inputs, from 1 to 99
for i in range(1, 100):
    steps.append(type_number(i))

plt.plot(steps) # execute the plotting
plt.title("O(1) - Constant Time") # Title label of the plot
plt.xlabel("Input Size") # x-axis label
plt.ylabel("No. of Steps") # y-axis label
plt.show() # displays the plot
