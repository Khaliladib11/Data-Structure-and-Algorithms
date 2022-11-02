# Merge Sort:
# - Runtime: O(nlog(n))
# - Space: O(n)

def mergesort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left_subarray = arr[:middle]
        right_subarray = arr[middle:]
        mergesort(left_subarray)
        mergesort(right_subarray)

        i = j = k = 0
        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] < right_subarray[j]:
                arr[k] = left_subarray[i]
                i += 1
            else:
                arr[k] = right_subarray[j]
                j += 1
            k += 1

        
        while i < len(left_subarray):
            arr[k] = left_subarray[i]
            i += 1
            k += 1
        
        while j < len(right_subarray):
            arr[k] = right_subarray[j]
            j += 1
            k += 1
    

if __name__ == '__main__':

    arr = [1, 2, 7, 4, -1]
    mergesort(arr)
    print(arr)
