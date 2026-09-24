"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size
Simulate customers joining/leaving.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random
queue = []

def initialise_queue(tempQueue):
    for i in range(random.randint(3,8)):
        tempQueue.append(chr(random.randint(65,90)))
    return(tempQueue)

def choose_action(action):
    while action.upper() != "NONE":
        if action.upper() == "ENQUEUE":
            queue.append(input("What would you like to enter?\n"))
            print("Added " + queue[len(queue) - 1] + " to queue.")
        elif action.upper() == "DEQUEUE":
            print(queue)
            try:
                removed = int(input("What is the position of the element you like to remove from queue (1 to " + str(len(queue)) +  ")\n"))
                queue.pop(removed - 1)
            except:
                print("Input error.")
        elif action.upper() == "PEEK":
            print("The first element in the queue is: " + queue[0])
        elif action.upper() == "SIZE":
            print("The length of the queue is: " + str(len(queue)))
        else:
            print("Action not recognised, please try again.")

        action = input("Choose an action: 'enqueue', 'dequeue', 'peek', 'size', or 'none'.\n")


if __name__ == "__main__":
    queue = initialise_queue(queue)
    choose_action(input("Choose an action: 'enqueue', 'dequeue', 'peek', 'size', or 'none'.\n"))