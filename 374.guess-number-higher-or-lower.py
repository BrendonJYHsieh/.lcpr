#
# @lc app=leetcode id=374 lang=python3
# @lcpr version=30113
#
# [374] Guess Number Higher or Lower
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        ans = (1 + n) // 2
        start = 0
        end = n
        while(guess(ans)!=0):
            if(guess(ans) == -1):
                end = ans
            elif(guess(ans) == 1):
                start = ans
            ans = (start + end) // 2

            if(start == ans):
                return n

        return ans

        
# @lc code=end



#
# @lcpr case=start
# 10\n6\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

# @lcpr case=start
# 2\n1\n
# @lcpr case=end

#

