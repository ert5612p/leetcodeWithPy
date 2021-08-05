class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict(zip(list(set(nums)), [nums.count(x) for x in set(nums)]))
        return max(dic, key = dic.get)
        
# Getting key with max value
a_dictionary = {"a": 1, "b": 2, "c": 3}
max_key = max(a_dictionary, key=a_dictionary.get)
print(max_key)

# Getting value with max value
a_dictionary = {"a": 1, "b": 2, "c": 3}
all_values = a_dictionary.values()
max_value = max(all_values)
print(max_value)
