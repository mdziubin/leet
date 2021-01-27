class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        best = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            sum2 = target-nums[i]
            l = i+1
            r = len(nums)-1

            while l<r:
                total = nums[l] + nums[r]
                if total == sum2:
                    return target
                elif total>sum2:
                    r -= 1
                else:
                    l += 1
                if abs(target-(total+nums[i])) < abs(best-target):
                    best = total+nums[i]
        return best