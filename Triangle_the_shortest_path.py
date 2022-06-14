def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    memo = [[-1] * len(triangle) for _ in range(len(triangle))]

    def main_body(triangle):
        if len(triangle) == 1:
            return triangle[0][0]

        elif check_seq(triangle, len(triangle) - 1):
            triangle1 = triangle[:len(triangle) - 1]
            return (triangle[len(triangle) - 1][0] + minimumTotal(triangle1))

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
            return triangle[0][0] + min(min1, min2)
        else:
            if triangle[0][0] == triangle[1][0] and triangle[0][0] == triangle[1][1]:
                return triangle[0][0] * len(triangle)
            else:
                return triangle[0][0] + min(triangle[1][1], triangle[1][0])

    result = main_body(triangle)
    return result



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



def minimumTotal_with_cache(triangle):
    memo = [[-1] * len(triangle) for _ in range(len(triangle))] # получаем пирамуду с одинаковыми значениями

    def dfs(i, j):
        if i == len(triangle): # У ОСНОВАНИЯ
            return 0
        if memo[i][j] != -1: # не основание
            return memo[i][j]

        lower_left = triangle[i][j] + dfs(i + 1, j)
        lower_right = triangle[i][j] + dfs(i + 1, j + 1)
        memo[i][j] = min(lower_left, lower_right)
        return memo[i][j]

    return dfs(0, 0)

