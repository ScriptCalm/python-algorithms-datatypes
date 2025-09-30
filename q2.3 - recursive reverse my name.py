# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework
print("student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework")
print() # space only
############################################################################

def reverse_myname(name, index, n):
    if index == n:  # base case
        return
    temp = name[index]  # storing each character in stack 
    reverse_myname(name, index+1, n)  # calling recursive function
    print(temp, end="")    # printing each character from stack (LIFO)


name = input("Enter your name: ") # input from user
n = len(name) # assign the lenght of the string to variable n
print("Output: ", end='') # formating output
reverse_myname(name, 0, n) # calling the recursive function
