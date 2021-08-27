class Solution:
    def climbStairs(self, n: int) -> int:
        output = [1,2]
        for i in range(2,n):
            temp = output[i-1] + output[i-2]
            output.append(temp)
        return output[n-1]
        