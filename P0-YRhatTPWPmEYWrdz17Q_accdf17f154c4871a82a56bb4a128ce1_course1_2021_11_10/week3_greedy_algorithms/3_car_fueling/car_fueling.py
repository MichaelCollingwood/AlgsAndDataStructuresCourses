# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops = [0] + stops + [distance]

    for stop1, stop2 in zip(stops[:-1], stops[1:]):
        if stop2 - stop1 > tank:
            return -1

    count = 0
    position = 0

    for stop1, stop2 in zip(stops[:-1], stops[1:]):
        if stop1 <= position + tank < stop2:
            count += 1
            position = stop1

    return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
