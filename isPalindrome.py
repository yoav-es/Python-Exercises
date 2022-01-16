12:10 15/01/2022 isPalindrome yoav eshed
class Solution:
    def isPalindrome(self, x: int) -> bool:
            num = str(x)
            res = helper(num, 0, len(num)-1)
            return res

def helper(x: chr, start: int, end: int) -> bool:
    if start >= end:
        return True
    elif x[start] != x[end]:
        return False
    else:
        return helper(x, start+1, end-1)