
def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)

if __name__ == '__main__':
    print(factorial(5))
