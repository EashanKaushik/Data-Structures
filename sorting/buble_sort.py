# time Complexity: O(n^2)
# space Complexity: O(1)
def bubble_sort(arr):

    current = 0
    next = 1
    last_index = len(arr)

    while last_index >= next:

        if arr[current] > arr[next]:
            arr[current], arr[next] = arr[next], arr[current]

        current += 1
        next += 1

        if next == last_index:
            current = 0
            next = 1
            last_index -= 1

if __name__ == '__main__':
    arr = [2, 3, 5, 6, 1]

    bubble_sort(arr)

    print(arr)
