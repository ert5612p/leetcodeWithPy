class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = '_'
            else:
                nums[i]

        for j in range(len(nums)):
            if nums[j] == '_':
                nums.remove('_')
                nums.append('_')
        return len([k for k in nums if k != '_'])
        