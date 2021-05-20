# space complexity O(1)
# time complexity O(nlogn)
def is_leaf(size, index):

    if index >= size // 2 and index <= size - 1:
        return True

    return False

def heapify(arr, size, index):

    if not is_leaf(size, index):
        left_child = (index * 2) + 1
        right_child = (index * 2) + 2

        if right_child < size:
            if arr[index] < arr[left_child] or arr[index] < arr[right_child]:
                if arr[right_child] > arr[left_child]:
                    arr[index], arr[right_child] = arr[right_child], arr[index]
                    heapify(arr, size, right_child)
                else:
                    arr[index], arr[left_child] = arr[left_child], arr[index]
                    heapify(arr, size, left_child)
        else:
            if left_child < size:
                if arr[left_child] > arr[index]:
                    arr[index], arr[left_child] = arr[left_child], arr[index]
                    heapify(arr, size, left_child)

def heapsort(arr):
    size = len(arr)

    # build heap
    for index in range(size//2 - 1, -1, -1):
        heapify(arr, size, index)

    # heap sort
    for index in range(size - 1, 0, -1):
        arr[0], arr[index] = arr[index], arr[0]
        heapify(arr, index, 0) # we will heapify for size 'index' and for element 0

if __name__ == '__main__':
    arr = [3, 6, 5, 0, 8, 2, 1, 9]
    # arr = [12, 11, 13, 5, 6, 7]

    heapsort(arr)

    print(arr)
