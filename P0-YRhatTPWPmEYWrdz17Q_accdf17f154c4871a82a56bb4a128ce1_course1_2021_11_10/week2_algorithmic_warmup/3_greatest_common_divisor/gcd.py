# Uses python3
import sys


def gcd_alg(a, b):
    if b == 0:
        return a, 0

    return gcd_alg(b, a % b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if a < b:
        print(gcd_alg(b, a)[0])
    else:
        print(gcd_alg(a, b)[0])