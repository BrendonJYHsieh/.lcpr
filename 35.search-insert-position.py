#
# @lc app=leetcode id=35 lang=python3
# @lcpr version=30113
#
# [35] Search Insert Position
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start_idx = 0
        end_idx = len(nums) - 1

        if(target > nums[end_idx]):
            return end_idx + 1
        if(target < nums[start_idx]):
            return 0

        while(1):
            mid_idx = (start_idx + end_idx) // 2
            mid = nums[mid_idx]

            if(target > mid):
                if(start_idx == mid_idx):
                    return start_idx + 1
                start_idx = mid_idx
            elif(target < mid):
                end_idx = mid_idx
            else:
                return mid_idx
                
        
# @lc code=end

# [1,3,5,7]\n6

#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#

