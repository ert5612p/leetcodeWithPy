class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        elif needle in haystack:
            i=0
            j=len(needle)
            while True:
                if haystack[i:i+j]==needle:
                    return i
                else:
                    i+=1
        else:
            return -1
    