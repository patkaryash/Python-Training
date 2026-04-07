import sys
class Stack:
    def __init__(self):
        self.stacklist=[]
    def push(self,value):
        self.stacklist.append(value)
    def displaystack(self):
        print("------====-----====-----=====-----====-----")
        print(self.stacklist)
        print("------====-----====-----=====-----====-----")
        print()
    def isEmpty(self):
        if self.stacklist==[]:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stacklist.pop()        
    def deletestack(self):
        self.stacklist=None  
        return "Stack is deleted" 
    def peekstack(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stacklist[-1]  
            
stackobj=Stack()
while True:
    
    print("1. Push")
    print("2. Display Stack element")
    print("3. Check is empty")
    print("4. Pop")
    print("5. Delete stack")
    print("6. Peek")
    print("7. Exit")
    print()
    print()
    
    choice =int(input("Enter your choice: "))
    print()
    if choice == 1:
        val=int(input("Enter value for stack "))
        stackobj.push(val)
    elif choice==2:
        stackobj.displaystack()    
    elif choice==3:
        print(stackobj.isEmpty())   
        print() 
    elif choice==4:
        print("Poped element is :",stackobj.pop())   
        print() 
    elif choice==5:
        stackobj.deletestack()  
    elif choice==6:
        print("The peek element is :",stackobj.peekstack()) 
        print()   
    elif choice==7:
        sys.exit()    
    else:
        print("Enter Right Choice")    
        print()