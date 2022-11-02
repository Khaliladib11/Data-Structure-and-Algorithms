# Stack follows the princle of last in first out (LIFO)


from inspect import stack


class Stack:

    def __init__(self):
        self.stack = []

    # add item on top of the stack
    def push(self, item):
        self.stack.append(item)
    
    # remove the top item of the stack
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    #return the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty or not
    def isEmpty(self):
        return True if len(self.stack) == 0 else False

    def display(self):
        print(self.stack)


if __name__ == '__main__':

    stack = Stack()
    print(stack.isEmpty())
    stack.push(1)
    stack.push(7)
    stack.push(12)
    stack.push(15)
    stack.display()

    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
    print(stack.isEmpty())