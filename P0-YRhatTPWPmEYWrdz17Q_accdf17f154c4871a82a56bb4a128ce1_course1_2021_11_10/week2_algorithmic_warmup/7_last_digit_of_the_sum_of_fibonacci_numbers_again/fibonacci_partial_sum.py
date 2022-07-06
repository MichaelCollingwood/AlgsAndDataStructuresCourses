# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, n):
    if n <= 1:
        return n

    _sum = 1
    prev, now = 0, 1
    for i in range(2, n+1):
        next = (prev + now) % 10
        prev = now
        now = next

    return _sum

def fibonacci_sum_naive(from_, n):
    if n <= 1:
        return n

    _sum = 1
    history = []
    repeating_history = False; it = 0
    prev, now = 0, 1
    for i in range(2, n+1):
        next = prev + now
        prev = now
        now = next

        if i > from_:
            _sum = (_sum+now) % 10

            if (prev, now) in history:
                start = history.index((prev, now))
                repeating_history = history[start:]
                it = i
                break
            else:
                history.append((prev, now))

    if repeating_history:
        _sum += (sum(repeating_history) % 10)*((n - it) // len(repeating_history)) % 10
        _sum += sum(repeating_history[:((n - it) % len(repeating_history))]) % 10

    return _sum



if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
