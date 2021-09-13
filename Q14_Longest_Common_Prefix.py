class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest=min(strs, key = len)
        if shortest != "":
            for i, s in enumerate(shortest):
                for l in strs:
                    if s != l[i]:
                        return l[:i]
        return shortest
        