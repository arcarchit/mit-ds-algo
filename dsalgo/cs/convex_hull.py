

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def jarvis_march(points):
    """
    Gift grapping algorithm

    Test Case
        ==  Given input
    Edge Cases
        ==  Colinear points
    Complexity
    :return:
    """
    BIG_NO = 2^10
    ans = []

    # Find leftmost point
    candidate = Point(BIG_NO, 0)
    for p in points:
        if p.x < candidate.x:
            candidate = p
    ans.append(candidate)


    # Start iteration
    current = candidate[-1]


    pass




def main():
    points = []
    points.append(Point(0, 3))
    points.append(Point(2, 2))
    points.append(Point(1, 1))
    points.append(Point(2, 1))
    points.append(Point(3, 0))
    points.append(Point(0, 0))
    points.append(Point(3, 3))

    jarvis_march(points)

