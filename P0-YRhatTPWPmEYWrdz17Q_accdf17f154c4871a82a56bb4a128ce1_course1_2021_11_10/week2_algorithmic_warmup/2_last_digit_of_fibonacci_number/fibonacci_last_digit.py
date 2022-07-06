# Uses python3
import sys


def get_fibonacci_last_digit_naive(num):
    if num <= 1:
        return num

    s = [0, 1]
    for _ in range(n - 1):
        s.append((s[-1] + s[-2]) % 10)

    return s[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
