import itertools
import math


def primes():
    p = 2
    yield p
    while True:
        p += 1
        # if (2 ** (p - 1) - 1) % p == 0: yield p          по теореме Ферма. Неверно для чисел Кармайкла (например, 561)
        if (math.factorial(p - 1) + 1) % p == 0: yield p  # по теореме Вильсона


if __name__ == '__main__':
    print(list(itertools.takewhile(lambda x: x <= 561, primes())))
