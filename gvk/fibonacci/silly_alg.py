def check_input_number(n):
    if n < 0: raise ValueError('It has to be >= 0')


def get_fibonacci_number(n):
    if n <= 1:
        return n
    else:
        return get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)


if __name__ == '__main__':
    n = int(input('Input a positive integer\n'))
    check_input_number(n)
    print(get_fibonacci_number(n))
