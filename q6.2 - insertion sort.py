# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework
print("student_dragos_gabriel_vornicu STUDENT ID:21490251 ADT coursework")

def insertionSort(alist):
    counter = 1
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        
        alist[position]=currentvalue
        print("Insertion Sort, Step ", counter, ":", alist)
        counter += 1


studentID = [2, 1, 4, 9, 0, 2, 5, 1]

print()
print("Initial list: ", studentID)
print()
insertionSort(studentID)







