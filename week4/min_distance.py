import math


def find_min_distance(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        return distance(arr[0], arr[1])
    mid = len(arr)//2
    left = find_min_distance(arr[0:mid])
    right = find_min_distance(arr[mid:len(arr)])
    if left == right:
        return 0
    return min(left, right)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))


def brute_force(p):
    min_val = float('inf')
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if distance(p[i], p[j]) < min_val:
                min_val = distance(p[i], p[j])

    return min_val


def strip_closest(points, dist):
    min_val = dist
    points.sort(key=lambda point: point.y)
    for i in range(len(points)):
        j = i+1
        while j < len(points) and (points[j].y-points[i].y < min_val):
            min_val = distance(points[i], points[j])
            j += 1
    return min_val


def closest_points(points):
    if len(points) <= 3:
        return brute_force(points)
    mid = len(points) // 2
    mid_point = points[mid]
    left = closest_points(points[0:mid])
    right = closest_points(points[mid:len(points)])
    dist = min(left, right)
    strip = list()
    for i in range(len(points)):
        if abs(points[i].x - mid_point.x) < dist:
            strip.append(points[i])
    return min(dist, strip_closest(strip, dist))


def closest(points):
    points.sort(key=lambda point: point.x)
    return closest_points(points)


if __name__ == "__main__":
    n = int(input())
    array = list()
    for i in range(n):
        p = Point(*(map(int, input().split())))
        array.append(p)

    # array = sorted(array, key=lambda x: x[0])
    print(round(closest(array), 6))
