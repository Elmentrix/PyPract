# this code is an implementation of a queue data structure
"""
List of methods of operation in a stack DS
1. push - adding item into the stack through the backside or index of the stack
2. pop - removing items from the stack from the last item position
3. peek - viewing through the stack at the last item
4. size - checking for the total number of items in the stack or size or length of the stack
5. isEmpty - checking an whether a stack is empty or not

The queue should be implemented as a class.
"""
from collections import deque
class Queue:
    # initial function for creating the queue variable
    def __init__(self):
        self.queue = deque()
        pass

    # push function for adding
    def push_a(self, item):
        self.queue.append(item)

    # pop function for deleting
    def pop_d(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None

    # string function to return the elements of the queue
    def __str__(self):
        return str(self.queue)

    # peek function
    def peek_s(self):
        # first checking if the stack is empty or not
        if self.queue:
            return self.queue[0]
        else:
            return None

    # size function
    def size(self):
        return len(self.queue)

    # isEmpty function
    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        else:
            return True

if __name__ == "__main__":
    queue = Queue()
    queue.push_a(100)
    queue.push_a(200)
    queue.push_a(300)
    queue.push_a(400)
    print(queue)
    queue.pop_d()
    print(queue)
    print(queue.isEmpty())
    queue.peek_s()
