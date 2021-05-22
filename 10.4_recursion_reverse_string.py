
def reverse_string(string):
    if len(string) == 0:
        return string

    return reverse_string(string[1:]) + string[0]

if __name__ == '__main__':

    print(reverse_string('Eashan'))
