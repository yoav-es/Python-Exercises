13:37 15/01/2022 romanToInt yoav eshed
class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        while i < len(s)-1:
            if helper(s[i]) < helper(s[i+1]):
                sum += helper(s[i+1]) - helper(s[i])
                i+=2
            else:
                sum += helper(s[i])
                i+=1
        if(i!= len(s)):
            sum += helper(s[i])
        return sum

def helper(s:str)->int:
    dict =  {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return dict.get(s,0)