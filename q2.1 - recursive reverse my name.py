# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework
print("student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework")
print() # empty space line
############################################################################


# recursive function
def reverse_myname(name):
    if len(name) == 0:  # base case
        return
     
    temp = name[0] # variable to store the stack frame of each recursion
    reverse_myname(name[1:]) # calling the function recursively (winding)
    print(temp, end='') # print stack one frame at the time (unwinding), on the same line



name = input("Enter your name: ") # Takes user input (name)

print("Output: ", end='') # formating the output
reverse_myname(name) # calling reverse_myname function with 'name' variable as parameter



