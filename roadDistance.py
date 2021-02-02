from geopy.distance import geodesic


def road_distance(points: list):
    res = 0
    for i in range(1, len(points)):
        # print(points[i])
        var1 = points[i - 1].split(",")
        x1 = var1[0]
        y1 = var1[1]
        var2 = points[i].split(",")
        x2 = var2[0]
        y2 = var2[1]
        res = res + geodesic((y1, x1), (y2, x2)).m
    return res
