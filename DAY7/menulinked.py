import sys

class Node:
    def __init__(self,data):
        self.data= data #instance variable
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def addnode(self,value):

        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node

    def displayNode(self):
        print("---------------------")
        while self.head is not None :
            print(self.head.data, '|','')
            self.head=self.head.next
            print()
        print("---------------------")
            
    def addbeginning(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node
            
        
    
    
    
            
if __name__ == '__main__':
    object=Linkedlist()

    while True:
        print()
        print("Menu Driven Linkedlist")
        print("1.Add node Linkedlist")
        print("2.Add Node in Beginning")
        print("3.Add Node in Between")
        print("4.Add Node in End")
        print("5.Display Linkedlist")
        print("6.Exit")

        choice=int(input("Enter your choice:"))
        if choice==1:
            value = int(input("Enter the value for node: "))
            object.addnode(value)
            print("Node added successfully in single linkedlist.")
        elif choice==5:
            print("Elements in the queue are:")
            object.displayqueue()