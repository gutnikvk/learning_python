if __name__ == '__main__':
    a, b = map(int, input('Input two integers').split())
    gcd = 1
    for d in range(1, max(a, b) + 1):
        if a % d == 0 and b % d == 0.0: gcd = d
    print(gcd)
    input()