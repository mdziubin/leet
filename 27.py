class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0

        length = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length
