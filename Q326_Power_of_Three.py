class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 0: 
            if n==1:
                return True
            elif n % 3 == 0:
                n = n / 3
            else:
                return False
        