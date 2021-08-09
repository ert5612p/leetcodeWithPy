class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        string_list=[l for l in s]
        list=[]
        for i in range(len(string_list)-1):
            if string_list[i] in dic:
                if dic[string_list[i]] >= dic[string_list[i+1]]:
                    list.append(dic[string_list[i]])
                else:
                    list.append(dic[string_list[i]]*-1)
        list.append(dic[string_list[-1]])
        return sum(list)
        