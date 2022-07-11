# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    if capacity == 0 or len(weights) == 0:
        return 0.

    prices = [v / w for v, w in zip(values, weights)]
    m = prices.index(max(prices))
    a = min(weights[m], capacity)
    value = prices[m] * a
    weights.pop(m)
    values.pop(m)

    return value + get_optimal_value(capacity - a, weights, values)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
