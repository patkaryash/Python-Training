class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
linkedlist = Linkedlist()

linkedlist.head = Node(5)  #first Node
second          = Node(10)
third           = Node(15)


#linking part
linkedlist.head.next= second
second.next= third

#display Linkedlist
                                                                