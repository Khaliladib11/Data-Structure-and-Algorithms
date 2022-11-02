# Linkedlist Data Structure

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # Insert item at the beginning of a list
    def insertAtBeginning(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    # insert a node in specific position
    def insert(self, prev, item):
        node = Node(item)
        
        self.node.next = self.prev.next
        self.prev.next = node

    # delete a node
    def deleteNode(self, position):
        if self.head is None:
            return None

        tmp = self.head
        
        if position == 0:
            self.head = tmp.next
            return

        for i in range(position-1):
            tmp = tmp.next
            if tmp is None:
                break

        if tmp is None or tmp.next is None:
            return

        next = tmp.next.next

        tmp.next = None
        tmp.next = next
            
    # seach for a node
    def seach(self, key):
        current = self.head

        while current:
            if current.data == key:
                return True
            current = current.next

        return False

    
    # insert item at the end of a list
    def insertAtTheEnd(self, item):
        node = Node(item)
        

        if self.head is None:
            self.head = node
            return

        last = self.head
        while last:
            last = last.next

        last.next = node

    # display the LinkedList
    def display(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.item, end=' ')
            tmp = tmp.next
    

if __name__ == '__main__':

    linkedList = LinkedList()
    linkedList.head = Node(1)
    second = Node(5)
    third = Node(9)
    linkedList.head.next = second
    second.next = third

    linkedList.display()