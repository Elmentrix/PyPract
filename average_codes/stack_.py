# this code is an implementation of a stack data structure
"""
List of methods of operation in a stack DS
1. push - adding item into the stack through the backside or index of the stack
2. pop - removing items from the stack from the last item position
3. peek - viewing through the stack at the last item
4. size - checking for the total number of items in the stack or size or length of the stack
5. isEmpty - checking an whether a stack is empty or not

The stack should be implemented as a class.
"""

class Stack:
    # initial function
    def __init__(self):
        self.items = []
        pass

    def __str__(self):
        return str(self.items)

    # push function
    def push(self, item):
        self.items.append(item)

    # pop function
    def pop(self):
        self.items.pop()
        pass

    # peek function
    def peek(self):
        # first checking if the stack is empty or not
        if self.items:
            return self.items[-1]
        else:
            return None

    # size function
    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None

    # isEmpty function
    def isEmpty(self):
        if len(self.items) > 0:
            return False
        else:
            return True

if __name__ == "__main__":
    stack = Stack()
    print("Empty: ", stack.isEmpty())
    print("Size of Stack: ", stack.size())
    stack.push(20)
    stack.push("word")
    stack.push(200)
    stack.push(4540)
    print("Stack Collection: ", str(stack))
    print("Size of Stack: ", stack.size())
    print("View from last: ", stack.peek())
    print("Empty: ", stack.isEmpty())
    print("Deleting item: ", stack.pop())
    print("Stack Collection: ", str(stack))
    print("Size of Stack: ", stack.size())
