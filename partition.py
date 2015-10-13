import sys

def partision(n, termsNum):
    counter = 0
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        p = a[:k + 1]
        if len(p) == termsNum:
            counter += 1
    return counter

def main(argv=None):
    n = int(input("Введите число для которого требуется вычислить количество разбиений: "))
    termsNum = int(input("Введите количество слагаемых в каждом разбиении: "))
    result = partision(n, termsNum)
    print("Существует %d разбиений(я) числа %d на %d слагаемых." % (result, n, termsNum))
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)