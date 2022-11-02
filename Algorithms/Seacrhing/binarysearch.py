# Binary Search:
# - Runtime: O(logn)
# - Space: O(1)

from msilib import MSIDBOPEN_DIRECT


def binarySearch(arr, x):

    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = low + (high - low) // 2
        if arr[middle] == x:
            return middle
        elif arr[middle] < x :
            low = middle + 1
        elif arr[middle] > x:
            high = middle -1
    return -1

def binarySearchRecursive(arr, x, low, high):
    if low > high: return -1

    middle = low + (high - low) // 2

    if arr[middle] > x:
        binarySearchRecursive(arr, x, low, middle-1)
    elif arr[middle] < x:
        binarySearchRecursive(arr, x, middle+1, high)
    else: return middle

if __name__ == '__main__':
    
    arr = [3, 4, 5, 6, 7, 8, 9]
    idx = binarySearch(arr, 4)
    print(idx)

    idx = binarySearchRecursive(arr, 6, 0, len(arr))
    print(idx)
