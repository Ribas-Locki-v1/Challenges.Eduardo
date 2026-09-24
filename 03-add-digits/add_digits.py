# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

def addDigits(num: int) -> int:

    print(num)

    if (num) < 10:
        return num
    else:
        text = str(num)
        count = 0
        for i in text:
            count += int(i)
        return addDigits(count)

# run tests
print(addDigits(0))
print(addDigits((99999999999)))
