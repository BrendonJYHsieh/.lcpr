#
# @lc app=leetcode id=50 lang=python3
# @lcpr version=30114
#
# [50] Pow(x, n)
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        
        if(n>0):
            if( n % 2 == 0):
                return self.myPow(x * x, n // 2)
            else:
                return self.myPow(x, n - 1) * x
        else:
            if( n % 2 == 0):
                return self.myPow(x * x, n // 2)
            else:
                return self.myPow(x, n + 1) / x
        
# @lc code=end



#
# @lcpr case=start
# 2.00000\n10\n
# @lcpr case=end

# @lcpr case=start
# 2.10000\n3\n
# @lcpr case=end

# @lcpr case=start
# 2.00000\n-2\n
# @lcpr case=end

#

