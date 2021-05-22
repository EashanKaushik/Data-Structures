
def fibonacci(number):
    if number <= 1:
        return number

    return fibonacci(number-1) + fibonacci(number-2)


if __name__ == '__main__':
    n_terms = 12

    if n_terms <= 0:
        print('Please enter number greater than zero')
    else:
        for term in range(n_terms):
            print(f'{term + 1}th term is {fibonacci(term)}')
