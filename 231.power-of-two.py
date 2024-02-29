#
# @lc app=leetcode id=231 lang=python3
# @lcpr version=30114
#
# [231] Power of Two
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 1:
            return True
        
        if n <= 0 or float(n)/2 != int(n/2):
            return False

        if(n < 1):
            return self.isPowerOfTwo(n * 2)
        else:
            return self.isPowerOfTwo(n/2)
        
# @lc code=end



#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 16\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

