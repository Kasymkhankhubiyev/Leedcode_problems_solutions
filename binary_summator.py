"""
Given two binary strings a and b, return their sum as a binary string.
"""

def addBinary(self, a: str, b: str) -> str:
    carry = 0
    long = ''
    short = ''
    result = ''
    if len(a) >= len(b):
      long = a[::-1]
      short = b[::-1]
    else:
      long = b[::-1]
      short = a[::-1]

    for i in range(len(short)):
      res = int(long[i])+int(short[i])+carry
      carry = res // 2
      result += str(res % 2)
    if len(long) - len(short) > 0:
      for i in range(len(short), len(long), 1):
          res = int(long[i]) + carry
          carry = res // 2
          result += str(res % 2)
    if carry == 1:
      result += '1';
    return result[::-1]
