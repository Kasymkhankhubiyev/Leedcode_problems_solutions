
def isValid(string):
    """
    путем подсчета, но подходит если только одинакове скобки???
    :param string:
    :return:
    """
    brackets_lib = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}':-3}
    #print(items)

    result = 0
    for i in range(len(string)):
        result += brackets_lib[string[i]]

    if result == 0:
        print('True')
    else:
        print('False')

def isValid2(s):
    string = s
    for _ in range(len(string)//2):
        if string == '':
            return True
        string = string.replace('()', '').replace('{}', '').replace('[]', '')
    return string == ''