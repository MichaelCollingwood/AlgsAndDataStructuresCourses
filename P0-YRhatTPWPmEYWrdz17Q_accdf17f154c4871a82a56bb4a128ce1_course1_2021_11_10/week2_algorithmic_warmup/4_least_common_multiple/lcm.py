# Uses python3
import sys


def gcd_alg(a, b):
    if b == 0:
        return a, 0

    return gcd_alg(b, a % b)


def lcm(a, b):
    return int(a * b / gcd_alg(a, b)[0])


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if a < b:
        print(lcm(b, a))
    else:
        print(lcm(a, b))
