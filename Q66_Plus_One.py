class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=0
        i=0
        j=len(digits)-1

        while j>=0:
            temp=digits[i]*(10**j)
            result+=temp
            i+=1
            j-=1
        result+=1
        
        return [i for i in str(result)]
        