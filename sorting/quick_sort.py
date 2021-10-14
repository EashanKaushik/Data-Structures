# quick sort O(nlogn) - Average if pivot is choosen wisely
# O(n^2) - Worse
# O(logn) - space complexity


# this implementaion has worst space complexity of O(n^2)
def quick_sort(arr, low, high):

    if low < high:

        pivot = partition(arr, low, high)
        
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):

    pivot = arr[high]
    lower_pivot = low - 1

    for compare in range(low, high):

        if arr[compare] <= arr[pivot]:
            lower_pivot += 1
            arr[lower_pivot], arr[compare] = arr[compare], arr[lower_pivot]
    
    arr[lower_pivot + 1], arr[high] = arr[high], arr[lower_pivot + 1]

    return lower_pivot + 1


if __name__ == '__main__':

    arr = [3, 7, 8, 5, 2, 1, 9, 5, 4]

    quick_sort(arr, 0, len(arr) - 1)

    print(arr)
