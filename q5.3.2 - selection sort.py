# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework
print("student_dragos_gabriel_vornicu STUDENT ID:21490251 ADT coursework")

def selectionSort(array, size):
    count = 1
    for ind in range(size):
        min_index = ind
        
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        print("Step ", count,":", array) # print array after each step
        (array[ind], array[min_index]) = (array[min_index], array[ind])
        count += 1
 
arr = [2, 1, 4, 9, 0, 2, 5, 1]
size = len(arr)

print()
print("Initial array: ")
print(arr)
print()


selectionSort(arr, size)

print()
print('Array after Selection Sort: ')
print(arr)





