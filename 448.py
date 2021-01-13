class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)

        stack = []
        for i in range(1, len(nums)+1):
            if i not in s:
                stack.append(i)

        return stack
