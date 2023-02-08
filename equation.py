def equation(a, b, c):
    if c < 0:
        return 'NO SOLUTION'
    if a == 0:
        if c ** 2 == b:
            return 'MANY SOLUTIONS'
        else:
            return 'NO SOLUTION'
    x = (c ** 2 - b) / a
    if x.is_integer():
        return int(x)
    else:
        return 'NO SOLUTION'




def main():
    a, b, c = [int(input()) for _ in range(3)]
    print(equation(a, b, c))


if __name__ == '__main__':
    main()
