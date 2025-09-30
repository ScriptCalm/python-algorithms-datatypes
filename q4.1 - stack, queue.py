# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework

# defining class Stack
class Stack:
    def __init__(self): # init method
        self.items = [] # initial stack as empty list

    def isEmpty(self): # method to check if stack is empty or not - O(1)
        return self.items == []

    def push(self, item):  # method to add items to the stack - O(1)
        self.items.append(item)

    def pop(self): # method to remove items from the stack - O(1)
        return self.items.pop()

    def peek(self): # method to return the top item in the stack - O(1)
        if self.items: # if the stack is empty return None
            return self.items[len(self.items) -1]
        return str(None) # None to type string (for concatenation)

    def size(self): # method to return the length of the stack - O(1)
        return len(self.items)

# defining class Queue
class Queue:
    def __init__(self): # init method
       self.items = [] # initial queue as empty list
       
    def is_empty(self): # check if the queue is empty or not - O(1)
       return self.items == []
    
    def size(self): # returns the size of the Queue (lenght of the list) - O(1)
       return len(self.items)
    
    def enqueue(self, item): # insert new item to the queue at index 0 - O(n)
       self.items.insert(0,item)
       
    def dequeue(self): # return and removes the earliest item of the Queue - O(1)
       return self.items.pop()
    
    def peek(self): # returns the first item in the queue - O(1)
        if self.items: # if the queue is empty return None
            return self.items[len(self.items) -1]
        return str(None) # None to type string (for concatenation)


# create objects for Stack and Queue classes
s = Stack()
q = Queue()
output = [] # variable to store the popped items from stack
            # and dequeued items from queue
            # (list)


# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework

### Defining Functions: ####################################################################
            
# function to print details of the stack at different stages
def stackReport():
    print("*** Stack report: ***")
    print("Total items in the stack: ", s.size())
    print("Show items of the stack: ", s.items)
    print("The top item of the stack is: " + s.peek() + " (last in)")
    print("Output: ", output)
    print() # output empty space line


# function that insert student ID digit by digit from left to right
def pushToStack(item):
    print("*** Push ID to stack, one digit at the time: ***")
    print() # output empty space line
    count = 1
    for i in item:
        print("* Step:", count, ", Push to stack: " + str(i))
        s.push(i)
        print("Show items of the stack: ", s.items)
        count += 1
        print() # output empty space line
    print() # output empty space line


# function for popping the items from stack digit by digit
def popFromStack(stack):
    print("*** Pop items, digit by digit: ***")
    print() # output empty space line
    count = 1
    for i in stack:
        print("* Stack after pop no.", count, ":", end=' ')
        output.append(s.pop()) # append the popped item to output
        print(s.items)
        print("Output: ", output)
        count += 1
        print() # output empty space line


# function for inserting the stack output to Queue
def insertToQueue(item):
    print("*** Insert output into the the Queue: ***")
    count = 1
    for i in item:
        print("* Step:", count, ", Enqueue: " + str(i))
        q.enqueue(i)
        print("Show items in the queue: ", q.items)
        count += 1
        print() # output empty space line
    output.clear() # clear the output
    print() # output empty space line

# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework

# function for emptying the queue digit by digit
def dequeueTheQueue(queue):
    print("*** Emptying the queue, digit by digit: ***")
    print() # output empty space line
    count = 1
    for i in queue:
        print("* Queue after dequeue no.", count, ":", end=' ')
        output.append(q.dequeue()) # append the removed item to output
        print(q.items)
        print("Output: ", output)
        count += 1
        print() # output empty space line


# function to print details of the Queue
def queueReport():
    print("*** Queue report: ***")
    print("Total items in the queue: ", q.size())    
    print("Show items in the queue: ", q.items)
    print("First item from queue: ", q.peek() + " (first in)")
    print("Output: ", output)
    print() # output empty space line


# calls both stack and queue report functions
def emptyProof():
    print("*** Both stack and queue are empty (proof): ***")
    print() # output empty space line

    stackReport() # run stack report
    queueReport() # calling queue report
    

def outputFormatting(section):
    print() # output empty space line
    print("=== Section:", section, "====================================================")
    print("student_dragos_gabriel_vornicu STUDENT ID:21490251 ADT coursework")
    print() # output empty space line
    print() # output empty space line

# student_dragos_gabriel_vornicu STUDENT ID: 21490251 ADT coursework

### Implementation: #######################################################################


### Section 1
outputFormatting(1)

emptyProof() # showing that both the stack and the queue are empty


### Section 2
outputFormatting(2) # formatting the output

studentID = input("Enter student id: ") # get input (student ID) from user
print("ID provided is: " + studentID)


### Section 3
outputFormatting(3) # formatting the output

pushToStack(studentID) # call pushToStack function
stackReport() # run stack report

### Section 4
outputFormatting(4) # formatting the output

popFromStack(s.items[:]) # call popFromStack function
stackReport() # run stack report

### Section 5
outputFormatting(5) # formatting the output

insertToQueue(output) # calling insertToQueue function
queueReport() # calling queue report

### Section 6
outputFormatting(6) # formatting the output

dequeueTheQueue(q.items[:])
queueReport() # calling queue report

### Section 7
outputFormatting(7) # formatting the output

print("Final Output: ", output)

print() 
print("========================= Transaction Completed ==========================")































