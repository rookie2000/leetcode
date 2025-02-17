class Solution:
    def search_lower(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1 #闭区间[left,right]
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target: #这种情况常用于实现 lower_bound（即找到第一个大于等于目标值的位置）。如果我们查找的是目标值，且我们希望找到它第一次出现的位置，应该把目标值与 mid 比较，如果相等也不马上返回，而是继续向左边缩小搜索范围。这是为了找到目标值的 最左侧 位置。
                right=mid-1 #区间[left,mid-1]
            else: 
                left=mid+1 #区间[mid+1,right]
        return left #如果目标值存在，left 就会停在目标值的 第一个位置（对于 lower_bound）；如果目标值不存在，left 将是目标值 应该插入的位置。
    def search(self, nums: List[int], target: int) -> int:
        n=self.search_lower(nums,target)
        if n<len(nums) and nums[n]==target:
            return n
        else:
            return -1
