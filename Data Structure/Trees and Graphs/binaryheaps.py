# Binary Heaps, complete binary tree:
# - Min-Heaps
# - Max -Heaps

# Worset Case scenario: 
# - Insert: O(log n) 
# - Extract: O(log n)

import sys
import math

class MinHeap:

    def __init__(self):
        self.heap = [0]
        self.current_size = 0


    def has_left_child(self, idx):
        """
        method to check if we has left child for item at index: idx
        """
        return ((2 * idx) + 1) <= len(self.heap)

    def has_right_child(self, idx):
        """
        method to check if we has right child for item at index: idx
        """
        return ((2 * idx) + 2) < len(self.heap)

    def get_left_child_idx(self, idx):
        """
        method to return the index of the left child if available, -1 otherwise
        """
        if self.has_left_child(idx):
            return (2 * idx) + 1
        else:
            return -1

    def get_right_child_idx(self, idx):
        """
        method to return the index of the right child if available, -1 otherwise
        """
        if self.has_right_child(idx):
            return (2 * idx) + 2
        else:
            return -1

    def get_parent_idx(self, idx):
        # the idx = 0 => means it is the min heap node
        if idx == 0:
            return -1
        
        # if the idx is in the heap
        elif idx <= len(self.heap):
            return math.floor(( idx - 1) / 2)

    
    def get_left_child(self, idx):
        left_idx = self.get_left_child_idx(idx)
        if left_idx > 0:
            return self.heap[left_idx]
        else:
            return None

    def get_right_child(self, idx):
        right_idx = self.get_right_child_idx(idx)
        if right_idx > 0:
            return self.heap[right_idx]
        else:
            return None

    def get_parent(self, idx):
        parent_idx = self.get_parent_idx(idx)
        if parent_idx > 0:
            return self.heap[parent_idx]
        else:
            return None

    def swap(self, first_idx, second_idx):
        if first_idx > len(self.heap) or second_idx > len(self.heap):
            return None

        else:
            tmp = self.heap[first_idx]
            self.heap[first_idx] = self.heap[second_idx]
            self.heap[second_idx] = tmp

    def heapify_up(self, child_idx=None):
        if child_idx is None:
            child_idx = len(self.heap) - 1

        parent_idx = self.get_parent_idx(child_idx)
        parent = self.heap[parent_idx]
        if parent and self.heap[child_idx] < parent:
            self.swap(child_idx, parent_idx)
            self.heapify_up(parent_idx)

    def heapify_down(self, idx=0):
        if idx >= len(self.heap) or not self.has_left_child(idx):
            return self.heap

        left_child_idx = self.get_left_child_idx(idx)
        right_child_idx = self.get_right_child_idx(idx)
        smaller_child_idx = None
        if self.heap[right_child_idx] < self.heap[left_child_idx]:
            smaller_child_idx = right_child_idx
        else:
            smaller_child_idx = left_child_idx

        if self.heap[idx] <= self.heap[smaller_child_idx]:
            return self.heap
        
        else:
            self.swap(idx, smaller_child_idx)
            return self.heapify_down(smaller_child_idx)


    def add(self, item):
        if type(item) == int:
            self.heap.append(item)
            self.heapify_up()

    def poll(self):
        if self.is_empty():
            print("The heap is empty")
            return None

        min_node = self.heap[0]
        self.heap = self.heap[-1]
        del self.heap[-1]
        self.heapify_down()
        return min_node

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if not self.is_empty():
            return self.heap[0]
        else:
            return None


if __name__ == '__main__':
    minHeap = MinHeap()
    minHeap.add(1)
    minHeap.add(10)
    minHeap.add(15)
    minHeap.add(2)
    minHeap.add(5)
    #minHeap.heap = [43, 19, 35, 12, 4, 2, 20, 6]
    minHeap.current_size = len(minHeap.heap)

    for i in range(minHeap.current_size):
        parent = minHeap.heap[i]
        left = minHeap.get_left_child(i)
        right = minHeap.get_right_child(i)
        if left is not None and right is not None:
            print(f"node: {parent}, leftchild: {left}, rightchild: {right}")
        
        elif left is not None:
            print(f"node: {parent}, leftchild: {left}.")
        
        else:
            print(f"node: {parent}")
