class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the root first
        l = 0
        r = len(nums)-1

        while l<r and nums[l]>nums[r]:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        
        root = l
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            realmid = (mid+root)%len(nums)
            if target == nums[realmid]:
                return realmid
            if target > nums[realmid]:
                l = mid+1
            else:
                r = mid-1
        return -1
            