def imp(lst, n):
    for i in range(n):
        lst.append(i)
    return lst


def fun(lst, n):
    return lst + list(range(0, n))


if __name__ == '__main__':
    lst = []
    lst = fun(lst, 10)
    print(lst)