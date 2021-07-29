# for

s = ["h", "e", "l", "l", "o"]
l = len(s)-1

output = []
for i in range(len(s)):
    temp = s[l-i]
    output.append(temp)
print(output)

# while
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        l = len(s)-1

        while i < l:
            s[i], s[l] = s[l], s[i]
            i += 1
            l -= 1
