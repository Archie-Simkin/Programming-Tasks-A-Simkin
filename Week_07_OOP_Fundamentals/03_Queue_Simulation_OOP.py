"""
TASK: 03 Queue Simulation Oop

# Imagine this is a queue of buses on the bus stop screen
Create class Queue:
- enqueue(x)
- dequeue()
- peek()
- size()
- is_empty()
Carry out a simulation of supermarket queue behaviour.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        try:
            return(self.queue.pop(0))
        except:
            return("Queue is empty.")

    def isEmpty(self):
        if len(self.queue) == 0:
            return(True)
        return(False)

    def peek(self):
        try:
            return(self.queue[0])
        except:
            return("Queue is empty.")

    def size(self):
        return(len(self.queue))


def choose_action(action):
    queue = Queue()
    while action.upper() != "NONE":
        if action.upper() == "ENQUEUE":
            queue.enqueue(input("What would you like to enter into the queue?\n"))
        elif action.upper() == "DEQUEUE":
            queue.dequeue()
        elif action.upper() == "PEEK":
            print("First item in queue is " + str(queue.peek()))
        elif action.upper() == "SIZE":
            print("Length of queue is " + str(queue.size()))
        elif action.upper() == "IS EMPTY":
            print(queue.isEmpty())
        else:
            print("Action not recognised, please try again.")

        action = input("Choose an action: 'enqueue', 'dequeue', 'peek', 'size', 'is empty' or 'none'.\n")


if __name__ == "__main__":
    choose_action(input("Choose an action: 'enqueue', 'dequeue', 'peek', 'size', 'is empty' or 'none'.\n"))
