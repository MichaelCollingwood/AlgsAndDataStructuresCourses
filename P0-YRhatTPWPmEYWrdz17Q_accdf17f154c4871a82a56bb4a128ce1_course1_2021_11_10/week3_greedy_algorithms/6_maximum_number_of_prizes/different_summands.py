# Uses python3
import sys
import math

def optimal_summands(n):
    k_raw = -0.5 + 0.5*math.sqrt(1 + 8*n)
    k = math.floor(k_raw)

    summands = list(range(1, k+1))
    summands[-1] += n - int(0.5*k*(k+1))
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
