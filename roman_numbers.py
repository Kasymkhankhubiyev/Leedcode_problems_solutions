def Roman_to_integer(string):
    Num_lib = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    string = 'MDLXX'
    result = 0
    numbers = []

    for i in range(len(string)):
        numbers.append(Num_lib[string[i]])

    print(numbers)

    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            result += numbers[i]
        else:
            if numbers[i] >= numbers[i + 1]:
                result += numbers[i]
            else:
                result -= numbers[i]
    return result

def Integer_to_Roman(num):
    num = num
    string = str(num)
    numbers = []
    result = ''
    Num_lib = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    for i in range(len(string) - 1, -1, -1):
        diff = num // 10 ** i
        num = num - diff * 10 ** i
        latter = Num_lib[10 ** i]
        if diff == 5:
            if latter == 'I':
                result += 'V'
            elif latter == 'X':
                result += 'L'
            elif latter == 'C':
                result += 'D'
        elif diff <= 3:
            result += latter * diff
        elif diff == 4:
            if latter == 'I':
                result += 'IV'
            elif latter == 'X':
                result += 'XL'
            elif latter == 'C':
                result += 'CD'
        elif diff == 9:
            if latter == 'I':
                result += 'IX'
            elif latter == 'X':
                result += 'XC'
            elif latter == 'C':
                result += 'CM'
        elif diff > 5:
            if latter == 'I':
                result += 'V' + 'I' * (diff - 5)
            elif latter == 'X':
                result += 'L' + 'X' * (diff - 5)
            elif latter == 'C':
                result += 'D' + 'C' * (diff - 5)

    return result

if __name__ == '__main__':

    string = 'LVIII'
    result = Roman_to_integer(string)
    print(string, result)

    num = 1994
    result1 = Integer_to_Roman(num)
    print(num, result1)
