"""
ou are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

[1,2,3]
[4,3,2,1]
[9]
[7,9,9,9,9]
[9,9,9,9,9]
"""

def plusOne(self, digits: List[int]) -> List[int]:
  numbers = digits[::-1]
  carry = (numbers[0] + 1) // 10
  numbers[0] = (numbers[0] + 1) % 10
  if carry > 0:
      for i in range(1, len(numbers), 1):
          res = numbers[i] + carry
          if res >= 10:
              carry = 1
              numbers[i] = res % 10
          else:
              numbers[i] = res
              carry = 0
      if carry == 1:
          numbers.append(1)
  return numbers[::-1]
        
