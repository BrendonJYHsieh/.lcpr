#
# @lc app=leetcode id=473 lang=python3
# @lcpr version=30113
#
# [473] Matchsticks to Square
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        length = sum(matchsticks) / 4

        ans = matchsticks.copy()

        for idx, item in enumerate(matchsticks):
            if(item == length):
                matchsticks.pop(idx)

            


        print(matchsticks)

        return False
# @lc code=end



#
# @lcpr case=start
# [1,1,2,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,4]\n
# @lcpr case=end

#

