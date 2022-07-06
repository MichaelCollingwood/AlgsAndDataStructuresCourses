# Uses python3
import sys


def calc_fib(n):
    if n <= 1:
        return n

    s = [0, 1]
    for _ in range(n-1):
        s.append(s[-2] + s[-1])

    return s[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(calc_fib(n))
