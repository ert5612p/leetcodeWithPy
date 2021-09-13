class Solution:
    def reverse(self, x: int) -> int:
        sigh = -1 if x<0 else 1
        s = str(x*sigh)
        temp = s[::-1]
        return 0 if int(temp)*sigh < -2**31 or int(temp)*sigh > 2**31 else int(temp)*sigh
