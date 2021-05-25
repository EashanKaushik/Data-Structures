import random

MIN_CHUNK = 32
# see video: https://www.youtube.com/watch?v=Yk4CBisILaw
# time Complexity- O(nlogn) worse
# O(n)- best
# O(nlogn)- avergae
# space Complexity- O(n)

# 1) this implementation takes static run size
# 2) galloping not implemented
# 3) efficient merging not implemented

# insertion_sort for all chunks of size 32
def insertion_sort(arr, start, end):

    index = start

    while index < end:
        next = index + 1
        if arr[next] < arr[index]:
            while next > start and arr[next] < arr[next - 1]:
                arr[next], arr[next - 1] = arr[next - 1], arr[next]
                next -= 1
        index += 1

# merging chunks
def merge_sort(arr, left_start, middle, right_end):
    length_right = right_end - middle

    if length_right > 0:
        length_left = middle - left_start + 1
    else:
        length_left = middle - left_start

    left_arr = arr[left_start:middle+1]
    right_arr = arr[middle + 1:right_end + 1]
    start_left = 0
    start_right = 0
    parent = left_start

    while start_left < length_left and start_right < length_right:
        if left_arr[start_left] <= right_arr[start_right]:
            arr[parent] = left_arr[start_left]
            start_left += 1
        else:
            arr[parent] = right_arr[start_right]
            start_right += 1

        parent += 1

    while start_left < length_left:
        arr[parent] = left_arr[start_left]
        start_left += 1
        parent += 1

    while start_right < length_right:
        arr[parent] = right_arr[start_right]
        start_right += 1
        parent += 1


def tim_sort(arr, size):

    # insertion_sort
    for index in range(0, size, MIN_CHUNK):
        insertion_sort(arr, index, min(index + MIN_CHUNK - 1, size - 1))

    sorted_chunk = MIN_CHUNK
    # merge sort
    while sorted_chunk < size:
        beg = 0
        while beg < size:
            end = min((beg + (2 * sorted_chunk)) - 1, size - 1)
            middle = min((beg + sorted_chunk) - 1, size)
            merge_sort(arr, beg, middle, end)
            beg += 2 * sorted_chunk
        sorted_chunk = 2 * sorted_chunk

# comparison of two arays for validation
def compare(arr1, arr2):
    is_equal = True

    for index, value in enumerate(arr1):
        if value != arr2[index]:
            is_equal = False

    print(is_equal)

if __name__ == '__main__':
    arr = [random.randint(1, 1000) for _ in range(random.randint(1000, 2000))]

    compare_array = arr.copy()

    print(f'Original Array: {arr}')

    size = len(arr)

    # sorting using user defined functions
    tim_sort(arr, size)

    print(f'Sorted Array: {arr}')

    # validation

    # sorting using python
    compare_array.sort()

    compare(arr, compare_array)
