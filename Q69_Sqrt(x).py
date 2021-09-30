#偷看解答QQ binaey search
class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        if x==1:
            return 1
        while l<=r:
            mid = (l+r)//2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid > x:
                r=mid
            else:
                l=mid
        