import sys
class Node:
    def __init__(self, data):
        self.data=data
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
#add node
    def addNode(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail
            
#add node in beginning
def addNodeBeginning(self, value):
    


if __name__== '__main__':
    object = LinkedList()
    
    while True:
        print('1. Add Node in LinkedList:')
        print('2. Add Node in beginning:')
        print('3. Add Node in between:')
        print('4. Add Node in end:')
        print('5. Display Linkedlist:')
        print('6. Exit:')
        
    ch = int(input("Enter your choice:"))
    if ch == 1:
        value = int(input('Enter value for node:'))
        object.addNode(value)
        print('Node added successfully in single Linkedlist:')

        