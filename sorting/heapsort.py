# time complexity- O(nlogn)
# space complexity- O(1)
def heap_sort(arr):
    size = len(arr)

    build_heap(arr, size) # O(n)

    for index in range(size - 1, 0, -1): # O(n)
        arr[0], arr[index] = arr[index], arr[0]
        heapify(arr, index, 0) # O(logn)

# we build heap for all nodes except leaf nodes
def build_heap(arr, size):
    for index in range(size // 2 - 1, -1, -1):
        heapify(arr, size, index)

# heapify arr of a particular size for index
def heapify(arr, size, index):

    if not is_leaf(size, index):

        left_child = 2 * index + 1
        right_child = 2 * index + 2

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

# checks if index is leaf index or not
def is_leaf(size, index):

    if index >= size // 2 and index < size:
        return True

    else:
        return False

if __name__ == '__main__':
    arr = [3, 6, 5, 0, 8, 2, 1, 9]

    heap_sort(arr)

    print(arr)
