# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework
print("student_dragos_gabriel_vornicu STUDENT ID:21490251 ADT coursework")

def selectionSort(a):
    counter = 1
    for slot in range(len(a)-1,0,-1):
       posOfMax=0
       for location in range(1,slot+1):
           if a[location]>a[posOfMax]:
               posOfMax = location

       temp = a[slot]
       a[slot] = a[posOfMax]
       a[posOfMax] = temp
       print("Selection Sort, Step ", counter, ":", a)
       counter += 1

studentID = [2, 1, 4, 9, 0, 2, 5, 1]

print()
print("Initial list: ", studentID)
print()
selectionSort(studentID)
print()
print("Student ID after Selection Sort: ", studentID)




