# O(n) when list almost sorted

# time Complexity: O(n^2)
# space Complexity: O(1)

# very efficient when len(arr) is small

def insertion_sort(arr):

    for index in range(len(arr) - 1):
        if arr[index] > arr[index + 1]:
            for inner_index in range(0, index + 1):
                if arr[index + 1] < arr[inner_index]:
                    arr[index + 1], arr[inner_index] = arr[inner_index], arr[index + 1]

def insertion_sort_two(arr):

    for index in range(1, len(arr)):

        key = arr[index]

        j = index - 1

        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j-= 1

        arr[j + 1] = key

if __name__ == '__main__':
    arr = [22, 4, 1, 100, 50, 70, 80, 68]

    # insertion_sort(arr)
    insertion_sort_two(arr)

    print(arr)
