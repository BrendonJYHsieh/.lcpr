#
# @lc app=leetcode id=120 lang=python3
# @lcpr version=30117
#
# [120] Triangle
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)

        for i in range(1, m):
            triangle[i][0] += triangle[i - 1][0]
            triangle[i][i] += triangle[i - 1][i - 1]
        
        for i in range(2, m):
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])

        return min(triangle[-1])

# @lc code=end



#
# @lcpr case=start
# [[2],[3,4],[6,5,7],[4,1,8,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[-10]]\n
# @lcpr case=end

