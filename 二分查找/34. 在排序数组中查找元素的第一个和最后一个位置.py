class Solution:
    def lower_bound(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1 #闭区间[left,right]
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target:
                right=mid-1 #范围缩小到[left,mid-1]
            else:
                left=mid+1 #范围缩小到[mid+1,right]
        return left
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=self.lower_bound(nums,target)
        if start==len(nums)or nums[start]!=target:
            return [-1,-1]
        end=self.lower_bound(nums, target+1)-1
        return [start,end]
