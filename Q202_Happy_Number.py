class Solution:
    def isHappy(self, n: int) -> bool:
        exist_list = []
        while n > 0:
            n = sum([int(i)**2 for i in str(n)])
            if n == 1:
                return True
            elif n in exist_list:
                return False
            else:
                exist_list.append(n)

