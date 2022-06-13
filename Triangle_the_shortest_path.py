def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """

    if len(triangle) == 1:
        return triangle[0][0]
    elif check_seq(triangle, len(triangle) - 1):
        triangle1 = triangle[:len(triangle) - 1]
        print(len(triangle), len(triangle1))
        return (triangle[len(triangle) - 1][0] + minimumTotal(triangle1))
    elif len(triangle) > 2:
        x1 = []
        for i in range(len(triangle) - 1):
            y1 = []
            for j in range(i + 1):
                y1.append(triangle[i + 1][j])
                # print(y1)
            x1.append(y1)
            # print(x1)

        x2 = []
        for i in range(len(triangle) - 1):
            y1 = []
            for j in range(i + 1):
                y1.append(triangle[i + 1][j + 1])
                # print(y1)
            x2.append(y1)
            # print(x2)
        min1 = minimumTotal(x1)
        min2 = minimumTotal(x2)
        if min1 > min2:
            return triangle[0][0] + min2
        else:
            return triangle[0][0] + min1
    else:
        if triangle[0][0] == triangle[1][0] and triangle[0][0] == triangle[1][1]:
            return triangle[0][0] * len(triangle)
        elif triangle[1][0] > triangle[1][1]:
            return triangle[0][0] + triangle[1][1]
        else:
            return triangle[0][0] + triangle[1][0]

def check_seq(triangle, i):
    run = True
    for k in range(len(triangle[i])):
        for j in range(k, len(triangle[i])):
            if triangle[i][k] != triangle[i][j]:
                run = False
                break
        if run == False:
            break
    return run