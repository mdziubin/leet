class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n, T = list(set(nums)), [float('-inf')]*3
        for i in n:
            if i > T[2]:
                T = [T[1], T[2], i]
            elif i > T[1]:
                T = [T[1], i, T[2]]
            elif i > T[0]:
                T = [i, T[1], T[2]]
        return T[0] if T[0] != float('-inf') else T[2]
