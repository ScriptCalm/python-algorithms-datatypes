# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework
print("student_dragos_gabriel_vornicu STUDENT ID:21490251 ADT coursework")


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    def get_data(self): # returns the self.data attribute
        return self.data
      
    def set_data(self, new_data): # replace the value of self.data with new_data
        self.data = new_data

    def get_next(self): # return the next attribute
        return self.next
        
    def set_next(self, new_next): # replace the current next with new_next attribute
        self.next = new_next

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item): # Function to add a node to the list
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def is_empty(self): # Returns True if the list is empty, False otherwise
        return self.head == None

    def size(self): # Returns the number of elements currently in the list
        curr = self.head
        count = 0
        while curr != None:
            count = count + 1
            curr = curr.get_next()
        return count
    
    def print_list(self): # Prints the data values of all nodes in the list
        curr = self.head
        while curr != None:
            print(curr.get_data(), end = ' ')
            curr = curr.get_next()
        print()

    def search(self, item): # Returns True if item found in list, False otherwise
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found


# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework

my_list = UnorderedList()  # Add code to create an UnorderedList object, 

studentID = "21490251" # The 8 numbers you will add them to the list should be your student ID

print()
print("Creating a linked list containing the following numbers: ", studentID)


# and call its add() function to add 8 items to the list
for i in studentID:
    my_list.add(i)


# Call the is_empty(), size() and print_list() functions to show that they work. 
print("Displaying the contents of the list using the print_list() function")
my_list.print_list()

print("Testig the is_empty() function")
print(my_list.is_empty())

print("Testig the size() function")
print(my_list.size())



print(my_list.search(93))















