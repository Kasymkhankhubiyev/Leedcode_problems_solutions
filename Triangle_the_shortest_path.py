def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """

    if len(triangle) == 1:
        return triangle[0][0]
    elif len(triangle) > 2:
        x1 = []
        for i in range(len(triangle) - 1):
            y1 = []
            for j in range(i + 1):
                y1.append(triangle[i + 1][j])
            x1.append(y1)

        x2 = []
        for i in range(len(triangle) - 1):
            y1 = []
            for j in range(i + 1):
                y1.append(triangle[i + 1][j + 1])
            x2.append(y1)
        min1 = minimumTotal(x1)
        min2 = minimumTotal(x2)
        if min1 > min2:
            return triangle[0][0] + min2
        else:
            return triangle[0][0] + min1
    else:
        if triangle[1][0] > triangle[1][1]:
            return triangle[0][0] + triangle[1][1]
        else:
            return triangle[0][0] + triangle[1][0]