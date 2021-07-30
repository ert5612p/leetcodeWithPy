class Solution:
    def addDigits(self, num: int) -> int:
        while int(num/10) != 0:
            num_list = [int(i) for i in str(num)]
            num = sum(num_list)
        return num
