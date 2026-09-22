# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x: int) -> bool:

    x = str(x)
    txt = x [::-1] 

    print(x,txt)
    return txt == str(x)

# run tests
print(isPalindrome(10))
print(isPalindrome(131))
