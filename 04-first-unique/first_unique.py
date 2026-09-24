# Given a string s, find the first non-repeating character in it and return its index.
# If it does not exist, return -1

def firstUniqChar(s: str) -> int:
    firstUniqChar = {}
    for char in s: 
        if char in firstUniqChar:
            firstUniqChar[char] += 1
        else:
            firstUniqChar[char] = 1
    for index, char in enumerate(s):
        if firstUniqChar[char] == 1:
            return index
    
    return -1

# run tests
print(firstUniqChar("banana"))
print(firstUniqChar("madam"))
print(firstUniqChar("aabb"))
