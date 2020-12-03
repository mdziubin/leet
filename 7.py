def revInt(num: int) -> int:
    # Preserve sign
    sign = 1
    if(num < 0):
        sign = -1

    # Convert absolute value of num to string
    strNum = str(abs(num))

    # Reverse string, convert to int, include sign
    reverse = sign * int(strNum[::-1])

    # Check overflow condition before returning
    return reverse if -(2**31) <= reverse <= 2**31 - 1 else 0


print(revInt(-24))
