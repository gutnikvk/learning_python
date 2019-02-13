def check_input_number(n):
    if n < 0: raise ValueError('It has to be >= 0')


def get_fibonacci_number_last_digit(n):
    fibonacciRow = []
    for i in range(n+1):
        if i<=1: fibonacciRow.append(i)
        else: fibonacciRow.append((fibonacciRow[i-1] + fibonacciRow[i-2]) % 10)
    return fibonacciRow[n]


if __name__ == '__main__':
    n = int(input('Input a positive integer\n'))
    check_input_number(n)
    print(get_fibonacci_number_last_digit(n))