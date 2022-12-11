def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i, j]
                return result

def check_int_number(string):
    """
    Проверяем является ли символ целым числом.
    :return:
    """
    for i in string: #нужно дополнить
        if i in '+-0123456789':
            pass
        else:return False
    return True

def get_numbers(string):
    """
    Из строки получаем числа
    -10^9 <= number <= 10^9
    -10^9 <= target <= 10^9
    :return: List[int]
    """
    nums = []
    errors = []
    numbers = string.split(', ')
    for num in numbers:
        print(num)
    for num in numbers:
        number = ''
        for j in range(len(num)):
            if (num[j] == '-' or num[j] == '+') and j == 0:
                number += num[j]
            elif num[j] in '1234567890':#['+', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                number += num[j]
            else:
                errors.append(num)
                break
        if len(number) == len(num):
            nums.append(int(number))

    for num in nums:
        print(num)

    if errors == []:
        return  nums
    else:
        print(f'Вы допустили ошибки в следующих аргументах: {errors}')
        return []

def check_exit(string):
    """
    Функция выхода из программы
    :param string:
    :return:
    """
    if string == 'Q' or string == 'q':
        return False
    else:
        return True


if __name__ == '__main__':
    """
    Можно добавить действия, когда произошла ошибка
    """
    run = True

    while run:
        print('Enter numbers, segregate with , ')
        numbers = input()
        print('Enter the target number')
        target = input()

        if check_int_number(target):
            nums = get_numbers(numbers)
            if nums != []:
                nums = get_numbers(numbers)
                result = twoSum(nums=nums, target=target)
                print(result)
                print(f'indixes are: [{result[0]}, {result[1]}]')
                print(f'Because {nums[result[0]]} + {nums[result[1]]} = {target}')

                print('Press Q to exit, and any to continue')
                state = input()
                run = check_exit(state)
        else: print(f'Значение taget={target} не число')
