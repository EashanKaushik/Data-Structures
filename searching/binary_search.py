# best time compleity- O(1)
# worst time compleity_ O(logn)

# space compleity- O(1)

# use when list is sorted

def binary_search(arr, value):

    length = len(arr)
    start = 0
    end = length - 1
    mid = (start + end) // 2

    while mid != start:

        if arr[mid] == value:
            return True
        elif arr[mid] > value:
            end = mid
        else:
            start = mid

        mid = (start + end) // 2

    if arr[start] == value or arr[end] == value:
        return True

    return False

if __name__ == '__main__':
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18]

    print(binary_search(arr, 16))
