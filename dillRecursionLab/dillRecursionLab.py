def main():
    print(fibRec(6))
    print(fibLoop(6))
    print(sumRec(100))
    print(sumLoop())

def fibRec(n):
    if n <=1:
        return n
    return fibRec(n - 1) + fibRec(n - 2)


def fibLoop(n):
    sum = 0
    current = 1
    previous =0

    for num in range(1, n):
        sum = previous + current
        previous = current
        current = sum

    return sum

def sumRec(n):
    if n == 1:
        return 1
    return n+sumRec(n-1)

def sumLoop():
    sum = 0

    for num in range(101):
        sum+=num

    return sum
main()