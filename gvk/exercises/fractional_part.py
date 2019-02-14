if __name__ == '__main__':
    input = input()
    if input.__contains__('.'):
        a = '0.' + input.split('.')[1]
    else: a = '0.0'
    print(a)
