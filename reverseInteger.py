import math
class Solution:
    def reverse(self, x: int) -> int:
        newNum = 0
        sign = 1
        if x<0:
            sign = 2
            x = -x
            digits = int(math.log(x,10)+1)
        if x>0:
            digits = int(math.log(x,10)+1)
        if x == 0:
            digits = 1
        for i in range(digits):
            digit = int(round((x/10-x//10)*10))
            newNum += int(digit*10**(digits-i-1))
            x = x//10
        if sign == 2:
            x = -newNum
        else:
            x = newNum
        if abs(x)>=2147483648:
            return 0
        return x