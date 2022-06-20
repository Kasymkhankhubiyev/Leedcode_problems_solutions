"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""

def mySqrt(self, x: int) -> int:
    sqr = 0
    if x == 1:
        return 1
    for i in range(x//2+1):
        if i*i <= x:
            if x - i*i < x - sqr*sqr:
                sqr = i
        else:
            break
    return sqr
        
