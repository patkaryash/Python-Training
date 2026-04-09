class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
linkedlist = LinkedList()

linkedlist.head = Node(5)  #first Node
second          = Node(10)
third           = Node(15)


#linking part
linkedlist.head.next= second
second.next= third 
third.next= fourth



#display Linkedlist
while linkedlist.head != None:
    print("|", linkedlist.head.data,"|", linkedlist.head.next,"->",end = "")
    linkedlist.head = linkedlist.head.next
    

