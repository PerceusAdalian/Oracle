def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge(L)
        merge(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insert(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick(left) + middle + quick(right)
    
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def dequeSort(arr):
    from collections import deque
    d = deque(arr)
    sorted_arr = []
    while d:
        min_val = min(d)
        sorted_arr.append(min_val)
        d.remove(min_val)
    return sorted_arr

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    
    merge(arr)
    print("Sorted array with Merge Sort:", arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    insert(arr)
    print("Sorted array with Insertion Sort:", arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble(arr)
    print("Sorted array with Bubble Sort:", arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    selection(arr)
    print("Sorted array with Selection Sort:", arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = quick(arr)
    print("Sorted array with Quick Sort:", sorted_arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    heapSort(arr)
    print("Sorted array with Heap Sort:", arr)

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = dequeSort(arr)
    print("Sorted array with Deque Sort:", sorted_arr)