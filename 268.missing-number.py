#
# @lc app=leetcode id=268 lang=python3
# @lcpr version=30113
#
# [268] Missing Number
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sum = len(nums) * (1 + len(nums)) // 2

        for num in nums:
            sum -= num

        return sum
            
        
# @lc code=end



#
# @lcpr case=start
# [3,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [9,6,4,2,3,5,7,0,1]\n
# @lcpr case=end

#

