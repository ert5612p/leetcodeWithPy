class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binary2int(s):
            result=0
            for i in range(len(s)):
                result+=int(s[i])*2**(len(s)-i-1)
            return result 
        n=binary2int(a)+binary2int(b)
        def int2binary(n):
            result=[]
            if n==0:
                return '0'
            while n>0:
                result.append(n % 2)
                n = n // 2
            return ''.join([str(i) for i in result[::-1]])
        return int2binary(n)
        