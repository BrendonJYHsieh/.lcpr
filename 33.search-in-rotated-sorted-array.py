#
# @lc app=leetcode id=33 lang=python3
# @lcpr version=30113
#
# [33] Search in Rotated Sorted Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_idx = 0
        end_idx = len(nums) - 1

        for index in range(0, len(nums) - 1, 1):
            if(nums[index] > nums[index + 1]):
                start_idx = index + 1 - len(nums)
                end_idx = index
                break

        if(target < nums[start_idx] or target > nums[end_idx]):
            return -1
        elif(nums[start_idx] == target):
                if(start_idx < 0):
                    start_idx += len(nums)
                return start_idx
        elif(nums[end_idx] == target):
                return end_idx
        
        while(1):
            mid_idx = (start_idx + end_idx) // 2

            mid = nums[mid_idx]

            if(start_idx == mid_idx or end_idx == mid_idx or start_idx == end_idx):
                return -1

            if(target > mid):
                start_idx = mid_idx
            elif(target < mid):
                end_idx = mid_idx
            else:
                if(mid_idx < 0):
                    mid_idx += len(nums)
                return mid_idx



        
# @lc code=end



#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

