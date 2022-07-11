# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # draw out diagram to understand this
    points = []
    segments = sorted(segments)
    min_end = segments[0][1]

    for seg1, seg2 in zip(segments[:-1], segments[1:]):
        if seg2[0] > min_end:
            points.append(seg1[0])
            min_end = seg2[1]

        min_end = min(min_end, seg2[1])

    points.append(segments[-1][0])

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
