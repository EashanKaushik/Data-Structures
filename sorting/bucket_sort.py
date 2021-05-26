# time Complexity- O(n^2)
# space Complexity- O(n)

# bueckt sort function
def bucket_sort(arr):

    # finding the maximum element
    max_element = max(arr) # O(n)

    count_arr = [[] for _ in range(0, 10)]
    output = list()

    # finding the division value to get the MSB of max_element
    division = 1
    while max_element / division >= 1:
        division *= 10

    division /= 10

    # adding the value in a bucket 0-9 based on its MSB
    for value in arr:
        index = int(value // division)
        print(index)
        count_arr[index].append(value)

    # apply insertion sort in individual buckets
    for index_array in count_arr:
        if index_array:
            insert_sort(index_array)
            output.extend(index_array)

    # changing original array (pass by reference)
    for index in range(0, len(arr)):
        arr[index] = output[index]

# insertion sort for individual buckets
def insert_sort(arr):
    next_index = 1

    while next_index < len(arr):

        curr_index = next_index - 1

        if arr[curr_index] > arr[next_index]:
            while curr_index >= 0:
                if arr[curr_index] > arr[next_index]:
                    arr[curr_index], arr[next_index] = arr[next_index], arr[curr_index]
                else:
                    break
                curr_index -= 1

        next_index += 1

if __name__ == '__main__':

    arr = [325, 569, 444, 129, 100, 989, 1000]

    bucket_sort(arr)

    print(arr)
