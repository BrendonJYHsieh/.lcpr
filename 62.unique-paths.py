#
# @lc app=leetcode id=62 lang=python3
# @lcpr version=30114
#
# [62] Unique Paths
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = []

        for i in range(m):

            temp = []

            for j in range(n):

                if(i == 0 or j == 0):
                    temp.append(1)
                else:
                    temp.append(0)
                    
            grid.append(temp)

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[-1][-1]

        
# @lc code=end



#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

#

