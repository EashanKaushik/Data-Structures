# time Complexity- O(n*k)
# space Complexity- O(n + k)

def count_sort(arr, division):
    count_arr = [0] * 10
    output = [0] * len(arr)

    # for every value in array we find the desired digit and count it
    for value in arr:
        index = value // division
        count_arr[index % 10] += 1

    # fining cumulative sum
    for index in range(1, 10):
        count_arr[index] += count_arr[index - 1]

     # starting from back of original list
    curr_index = len(arr) - 1

    # we update output list
    while curr_index >= 0:
        value = (arr[curr_index] // division) % 10
        count_arr[value] -= 1
        new_index = count_arr[value]

        output[new_index] = arr[curr_index]

        curr_index -= 1

    return output

def radix_sort(arr):

    # max element in array
    max_element = max(arr) # O(n)

    division = 1

    # we will run the code for number of digits in max element 'k'
    while max_element / division >= 1: # O(k)

        # we will sort from LSB to MSB while updating original array
        arr = count_sort(arr, division)
        division *= 10

    return arr

if __name__ == '__main__':
    arr = [312, 1, 400, 1758, 10, 800, 2, 0, 5]

    print(radix_sort(arr))
