#stack implementation using list
stack=[]
def push():
    element=int(input("Enter the element:"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("Stack is empty")
    else:
        e=stack.pop()
        print("Removed Element:",e)
        print(stack)
while True:
    print("Select operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("In between 1-3")
