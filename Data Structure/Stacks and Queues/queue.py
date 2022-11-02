# Queue follows the princle of first in first out (FIFO)


from symbol import pass_stmt


class Queue:

    def __init__(self):
        self.queue = []

    # add item to the queue
    def add(self, item):
        self.queue.append(item)
    
    # remove item from the queue
    def remove(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def peek(self):
        return self.queue[-1]

    def isEmpty(self):
        return True if len(self.queue) == 0 else False

    def display(self):
        print(self.queue)


if __name__ == '__main__':

    queue = Queue()
    print(queue.isEmpty())
    queue.add(1)
    queue.add(8)
    queue.add(3)
    queue.add(4)
    queue.display()
    print(queue.isEmpty())
    print(queue.remove())
    print(queue.remove())
    print(queue.remove())
    print(queue.isEmpty())
    print(queue.peek())