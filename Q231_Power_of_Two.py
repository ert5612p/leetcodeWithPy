# Time Limit Exceeded
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while True:
            if n == 1:
                return True
                break
            elif n % 2 == 0:
                n = n / 2
            else:
                return False
                break


# pass
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0:
            if n == 1:
                return True
                break # 其實不用 break
            elif n % 2 == 0:
                n = n / 2
            else:
                return False
                break # 其實不用 break

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0:
            if n == 1:
                return True
            elif n % 2 == 0:
                n = n / 2
            else:
                return False