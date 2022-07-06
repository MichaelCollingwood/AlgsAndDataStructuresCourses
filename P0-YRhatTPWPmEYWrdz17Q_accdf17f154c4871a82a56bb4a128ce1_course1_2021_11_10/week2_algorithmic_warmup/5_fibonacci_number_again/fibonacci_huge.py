# Uses python3
import sys


def calc_fib(n, m):
    if n <= 1:
        return n

    history = []
    repeating_history = False; it = 0
    prev, now = 0, 1
    for i in range(2, n+1):
        next = (prev + now) % m
        prev = now
        now = next
        if (prev, now) in history:
            start = history.index((prev, now))
            repeating_history = history[start:]
            it = i
            break
        else:
            history.append((prev, now))

    if repeating_history:
        now = repeating_history[(n-it) % len(repeating_history)][1]

    return now


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(calc_fib(n, m))
