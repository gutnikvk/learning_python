def euclid_gcd(a, b):
    if a == 0: return b
    if b == 0: return a
    if a >= b: return euclid_gcd(a % b, b)
    else: return euclid_gcd(a, b % a)


if __name__ == '__main__':
    a, b = map(int, input('Input two integers').split())
    print(euclid_gcd(a, b))
    input()