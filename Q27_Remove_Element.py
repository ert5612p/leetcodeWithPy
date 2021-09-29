class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)
            nums.append("_")
        return len([n for n in nums if n != "_"])
        