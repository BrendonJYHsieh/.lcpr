#
# @lc app=leetcode id=169 lang=python3
# @lcpr version=30113
#
# [169] Majority Element
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        table = {}
        max = 0
        ans = 0

        for num in nums:
            if num not in table.keys():
                table[num] = 1
                if(table[num] > max):
                    max = table[num]
                    ans = num
            else:
                table[num] += 1
                if(table[num] > max):
                    max = table[num]
                    ans = num
        return ans

        # nums.sort()
        # return nums[len(nums)//2]
        
# @lc code=end



#
# @lcpr case=start
# [3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end

#

