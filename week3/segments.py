# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments = sorted(segments, key=lambda x: x[1])
    coords = []

    index = 1
    max_right = segments[0].end
    coords.append(max_right)
    while index < len(segments):
        if max_right < segments[index].start:
            max_right = segments[index].end
            coords.append(max_right)
        index += 1

    return coords


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
