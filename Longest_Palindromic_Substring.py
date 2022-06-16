
def longestPalindrome(s):
    string = s

    def isPalindrome(s):
        invers = s[::-1]
        print(invers)
        if s == invers:
            return True
        else: return False

    return isPalindrome(string)