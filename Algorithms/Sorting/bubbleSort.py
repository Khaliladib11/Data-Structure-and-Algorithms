

def bubbleSort(arr):
    # Runtime: average case and worset case: o(n^2)
    # Memory: O(1) 
    
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                swapped = True

        if not swapped:
            break

    
    return arr


if __name__ == '__main__':

    arr = [-2, 45, 0, 11, -9]

    print(bubbleSort(arr))