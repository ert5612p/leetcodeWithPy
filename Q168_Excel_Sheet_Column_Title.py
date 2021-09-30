##沒有想到(columnNumber-1)的部分QQ
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        from string import ascii_uppercase
        letter=[x for x in ascii_uppercase]
        number = [i for i, _ in enumerate(letter, start=1)]
        LETTERS=dict(zip(number,letter))
        result=[]
        while columnNumber>0:
            if columnNumber % 26 ==0:
                result.append('Z')
            else:
                result.append(LETTERS[columnNumber % 26])
            columnNumber = (columnNumber-1) // 26
        return ''.join(result[::-1])
        