class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        from string import ascii_uppercase
        letter=[x for x in ascii_uppercase]
        number = [i for i, _ in enumerate(letter, start=1)]
        LETTERS=dict(zip(letter, number))
        
        l = len(columnTitle)-1
        output = 0
        for character in columnTitle:
            temp = 26 ** l * LETTERS[character]
            l-=1
            output += temp
        return output