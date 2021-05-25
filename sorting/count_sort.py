# time Complexity- O(n + k)
# space Complexity- O(n + k)

# doesnt work for negative numbers

def count_sort(arr):
    count_arr = [0] * (max(arr) + 1) # time Complexity- O(n)
    output = [0] * len(arr)

    # count array
    for value in arr: # O(n)
        count_arr[value] += 1

    # cumulative sum
    for index in range(1, len(count_arr)): # O(n-1)
        count_arr[index] += count_arr[index - 1]

    # start from the last index
    index = len(arr) - 1

    # iterate backwards
    while index >= 0:
        value = arr[index]
        count_arr[value] -= 1
        new_index = count_arr[value]
        output[new_index], arr[index] = arr[index], output[new_index]
        index -= 1

    return output

if __name__ == '__main__':

    arr = [1, 3, 2, 3, 2, 1, 4, 5, 5, 4, 6, 6, 4, 7]

    output = count_sort(arr)

    print(output)

    arr = [22, 4, 1, 100, 50, 70, 80, 68]

    print(count_sort(arr))
