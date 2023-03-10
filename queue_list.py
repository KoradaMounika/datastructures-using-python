#queue implementation using list
queue=[]
def enqueue():
    element=int(input("Enter the element:"))
    queue.append(element)
    print(queue)
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e=queue.pop(0)
        print("Removed Element:",e)
        print(queue)
def display():
    print(queue)
while True:
    print("Select operation 1.enqueue 2.dequeue 3.show 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("In between 1-4")

