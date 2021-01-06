class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.helper(nums, target, 4, [], results)
        return results
    
    def helper(self, nums, target, N, res, results):
        if len(nums)<N or N<2:
            return
        
        if N == 2:
            two_output = self.twoSum(nums, target)
            if two_output:
                for arrs in two_output:
                    results.append(arrs + res)
        else: 
            for i in range(len(nums) - N +1):
                if nums[i]*N > target or nums[-1]*N < target:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.helper(nums[i+1:], target-nums[i], N-1, res + [nums[i]], results)
    
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        res = []
        
        while l<r:
            temp = nums[l]+nums[r]
            if temp == target:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif temp>target:
                r-=1
            else:
                l+=1
                                        
        return res