def minimumTotal(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """

    # нужна рекурсивная функция

    summ = triangle[0][0]
    iterr = 0
    for i in range(1, len(triangle)):
        if triangle[i][iterr] > triangle[i][iterr + 1]:
            summ += triangle[i][iterr + 1]
            iterr = iterr + 1
        elif triangle[i][iterr] < triangle[i][iterr + 1]:
            summ += triangle[i][iterr]
        else:
            if triangle[i + 1][iterr] < triangle[i + 1][iterr + 2]:
                summ += triangle[i][iterr]
            else:
                summ += triangle[i][iterr + 1]
                iterr = iterr + 1

    return summ

