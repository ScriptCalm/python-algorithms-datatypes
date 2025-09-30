# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework
print("student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework")
print() # space only
############################################################################
from functools import wraps

def reverse_myname(name):
    if len(name) == 0:
        return
     
    temp = name[0]
    reverse_myname(name[1:])
    print(temp, end='')


# Recursion Visualisation Function ##########################################   
def trace(func):
    # Store function name, for later use
    func_name = func.__name__
    separator = '|  '  # Used in trace display

    # Set the current recursion depth
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs):
        # Display function call details
        print(f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})')
        # Begin recursing
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        # Exit current level
        trace.recursion_depth -= 1
        # Display return value
        print(f'{separator * (trace.recursion_depth + 1)}|-- return {result}')

        return result

    return traced_func
# End of Recursion Visualisation Function ###################################

name = input("Enter your name: ")
print() # empty space line

print("Recursion Stages:")
reverse_myname = trace(reverse_myname)
reverse_myname(name)



