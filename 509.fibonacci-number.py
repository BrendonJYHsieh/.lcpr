#
# @lc app=leetcode id=509 lang=python3
# @lcpr version=30114
#
# [509] Fibonacci Number
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

