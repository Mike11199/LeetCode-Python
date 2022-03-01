from turtle import ycor
from typing import List

from numpy import zeros

#parameters
x = 15433451      #s/b true
y = 1331     #s/b true
z = 112      #s/b false


def isPalindrome(x: int) -> bool:
    if x < 0 or (x > 0 and x%10 == 0):   
     return False

    reversedNum = 0

    while x > reversedNum:
        reversedNum = reversedNum * 10 + x % 10
        x = x // 10

    # If x is equal to reversed number then it is a palindrome
    # If x has odd number of digits, dicard the middle digit before comparing with x
    # Example, if x = 23132, at the end of for loop x = 23 and reversedNum = 231
    # So, reversedNum/10 = 23, which is equal to x
    return True if (x == reversedNum or x == reversedNum // 10) else False


test = isPalindrome(x)
print(test)