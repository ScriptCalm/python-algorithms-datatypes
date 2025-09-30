# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework
print("student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework")
print() # space only
############################################################################

number = [20, 15, 18, 9, 5]

def function_n_squared(number):
    n = len(number) # O(1)
    for i in range(n): # O(n)
        print("outer loop")
        print(i)
        for j in range(n): # O(n)
            result = number[i] + number[j] # O(1)
            print("inner loop")
            print(j)
            print(result)
    return result # O(1)

print(function_n_squared(number))
print(len(number))

