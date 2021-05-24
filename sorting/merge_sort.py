def merge_sort(arr):

    if len(arr) > 1:

        # middle of length of array
        mid_index = len(arr) // 2

        # left and right arrays
        left = arr[:mid_index]
        right = arr[mid_index:]

        # we want to sort both left and right arrays
        merge_sort(left)
        merge_sort(right)

        # sorting the parent according to sorted left and right children
        left_index = right_index = parent_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                arr[parent_index] = left[left_index]
                left_index += 1
            else:
                arr[parent_index] = right[right_index]
                right_index += 1
            parent_index += 1

        # remaining children are added first we add left than right children
        while left_index < len(left):
            arr[parent_index] = left[left_index]
            left_index += 1
            parent_index += 1

        while right_index < len(right):
            arr[parent_index] = right[right_index]
            right_index += 1
            parent_index += 1

if __name__ == '__main__':
    arr = [22, 4, 1, 100, 50, 40, 70, 90, 80]

    merge_sort(arr)

    print(arr)
