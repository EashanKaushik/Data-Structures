def return_after_n_recursion_one(n):

    return_after_n_recursion_one(n-1)

def return_after_n_recursion_two(n):
    if n < 3: # Base return: identify a condition after which you will start returning
        return 'Cap'

    return_after_n_recursion_two(n-1)

def return_after_n_recursion(n):
    if n < 3: # Base return: identify a condition after which you will start returning
        return 'Cap'

    return return_after_n_recursion(n-1) # recursive return

if __name__ == '__main__':
    # Stack overflow
    # print(return_after_n_recursion_one(5))

    # return none
    print(return_after_n_recursion_two(5))

    # correct fucntion
    print(return_after_n_recursion(5))

    # recursive fucntions usually should have two returns
    # inside classes while recursively looping class variables that might not be the case
