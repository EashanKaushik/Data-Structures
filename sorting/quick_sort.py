# quick sort O(nlogn) - Average if pivot is choosen wisely
# O(n^2) - Worse
# O(logn) - space complexity


# this implementaion has worst space complexity of O(n^2)
# def quick_sort(arr):
#     if len(arr) > 1:
#         pivot = arr.pop()
#         items_less = [item for item in arr if item < pivot]
#         items_greater = [item for item in arr if item >= pivot]
#
#         return quick_sort(items_less) + [pivot] + quick_sort(items_greater)
#     else:
#         return arr

# better implementaion
def quick_sort(arr, left, right):

    if left < right:

        start = left
        end = right - 1
        pivot = right

        while start < pivot:

            if arr[pivot] < arr[start]:
                if pivot == start + 1:
                    arr[pivot], arr[start] = arr[start], arr[pivot]
                    pivot -= 1
                    continue
                arr[pivot - 1], arr[pivot] = arr[pivot], arr[pivot - 1]
                arr[pivot], arr[start] = arr[start], arr[pivot]
                pivot -= 1
                continue

            start += 1

        quick_sort(arr, left, pivot - 1)

        quick_sort(arr, pivot + 1, right)

if __name__ == '__main__':

    arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]

    quick_sort(arr, 0, len(arr) - 1)

    print(arr)
