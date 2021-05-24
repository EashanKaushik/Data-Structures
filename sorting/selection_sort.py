# time Complexity: O(n^2)
# space Complexity: O(1)
def selection_sort(arr):

    for index in range(len(arr)):
        min_index = index
        for inner_index in range(index+1, len(arr)):


            if arr[min_index] > arr[inner_index]:
                min_index = inner_index

        arr[index], arr[min_index] = arr[min_index], arr[index]

if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]

    selection_sort(arr)

    print(arr)
