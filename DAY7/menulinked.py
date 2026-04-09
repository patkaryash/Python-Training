

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
        print("--------------------------------------")
        temp=self.head
        while temp!=None:
            print("!",temp.data,"!-->",end="")
            temp=temp.next
        print()
        print("--------------------------------------")
        
            
    def addbeginning(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node

    def addbetween(self,index , value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        elif index ==0:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
    
    def addend(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    
    def deleteNode(self,value):
        temp=self.head
        if temp is not None:
            if temp.data==value:
                self.head=temp.next
                temp=None
                return
        while temp is not None:
            if temp.data==value:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return
        prev.next=temp.next
        temp=None
        
    def searchNode(self,value):
        temp=self.head
        while temp!=None:
            if temp.data==value:
                return True
            temp=temp.next
        return False
    
        
        
    
            
if __name__ == '__main__':
    object=Linkedlist()

    while True:
        print()
        print("Menu Driven Linkedlist")
        print("1.Add Node in Linkedlist")
        print("2.Add Node in Beginning")
        print("3.Add Node in Between")
        print("4.Add Node in End")
        print("5.Display Linkedlist")
        print("6.Delete Node")
        print("7.Search Node")
        print("8.Exit")

        choice=int(input("Enter your choice:"))
        if choice==1:
            value = int(input("Enter the value for node: "))
            object.addnode(value)
            print("Node added successfully in single linkedlist.")
        elif choice==2:
            value = int(input("Enter the value for node: "))
            object.addbeginning(value)
            print("Node added successfully in single linkedlist.")
        elif choice==3:
            value = int(input("Enter the value for node: "))
            pos = int(input("Enter the position for node: "))
            object.addbetween(value,pos)
            print("Node added successfully in single linkedlist.")
        elif choice==4:
            value = int(input("Enter the value for node: "))
            object.addnode(value)
            print("Node added successfully in single linkedlist.")
        elif choice==5:
            print("Elements in the queue are:")
            object.displayNode()
        elif choice==6:
            value=int(input("Enter the value to be deleted:"))
            object.deleteNode(value)
        elif choice==7:
            value=int(input("Enter the value to be searched:"))
            if object.searchNode(value):
                print("Node found")
            else:
                print("Node not found")
        elif choice==8:
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")