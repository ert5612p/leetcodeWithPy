# Time Limit Exceeded
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = dict(zip(list(set(nums)), [nums.count(x) for x in set(nums)]))
        for key, value in dic.items():
            if value > 1:
                return True
        return False

# smart method
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
