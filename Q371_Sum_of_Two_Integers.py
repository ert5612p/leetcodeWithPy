class Solution:
    def getSum(self, a: int, b: int) -> int:
        import math
        return round(math.log((10**a)*(10**b),10))
        