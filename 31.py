class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[2,3,6,5,4,1]]
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return 

        while nums[j] <= nums[i-1]:
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]

        #Reverse everything to the right of i-1
        l = i
        r = len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        return
        
            
        
                