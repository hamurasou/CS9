
def integerDivision(n, k):
    if n < k:
        return 0
    return integerDivision(n - k, k) + 1

def collectEvenInts(listOfInt):
    if not listOfInt:
        return []
    if listOfInt[0] % 2 == 0:
        return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
    return collectEvenInts(listOfInt[1:])

def countVowels(someString):
    if not someString:
        return 0
    if someString[0] in 'AEIOUaeiou':
        return 1 + countVowels(someString[1:])
    return countVowels(someString[1:]) 

def reverseString(s):
    if not s:
        return ""
    return reverseString(s[1:]) + s[0]

def removeSubString(s, sub):
    if sub not in s:
        return s
    first_at = s.find(sub)
    s_rest = s[:first_at] + s[first_at + len(sub):]
    return removeSubString(s_rest, sub)


