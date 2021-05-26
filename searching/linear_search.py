# best case- O(1)
# worse case- O(n)

# space compleity- O(1)

# generally used when list is not sorted
def linear_search(arr, value):

    if value in arr:
        return True

    return False

if __name__ == '__main__':
    arr = [100, 230, 56, 1, 5, 8]

    print(linear_search(arr, 1))
