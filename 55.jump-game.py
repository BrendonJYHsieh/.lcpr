#
# @lc app=leetcode id=55 lang=python3
# @lcpr version=30114
#
# [55] Jump Game
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        start_idx = 0
        length = len(nums)

        if(length == 1):
            return True

        while 1:
            max = -1
            idx = start_idx
            for i in range(1, nums[start_idx] + 1):
                if(start_idx + i >= length):
                    return True

                if(nums[start_idx + i] + start_idx + i > max):
                    max = nums[start_idx + i] + start_idx + i 
                    idx = start_idx + i

            if(idx == start_idx):
                return False

            start_idx = idx
            
            if start_idx >= len(nums) - 1:
                return True
        
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#

