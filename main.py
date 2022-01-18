from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    pref = ""
    index = 0
    cpy = strs
    helper(index, pref, strs)
    while(len(cpy)>0):
        helper(index, pref, cpy)
        index+=1
    return pref
###

def helper(index,pref,cpy) -> str:
    dic = {}
    for dm in range(len(cpy)):
        loc = cpy[dm]
        if len(loc) > index:
            return pref
        if cpy[dm][index] in dict:
            dict[cpy[dm][index]] += 1
        else:
            dict[cpy[dm][index]] = 1
        if(index>1):
            cpy.pop(dm)
    pref += getMaxVal(dic)
    return pref


def getMaxVal(letters) -> str:
    maxLetter = ""
    first_key = ""
    marklist = sorted((value, key) for (key, value) in letters.items())
    max_value = max(letters.values())
    if max_value > 1:
        first_key = list(letters.keys())[0]
    if letters.values()[0] >= letters.values()[1]:
       maxLetter += first_key
    return maxLetter

print(longestCommonPrefix(["lower","flow","flight"]))





