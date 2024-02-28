#
# @lc app=leetcode id=63 lang=python3
# @lcpr version=30114
#
# [63] Unique Paths II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if(obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1):
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        grid = []

        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(0)

            grid.append(temp)

        grid[0][0] = 1

        for i in range(0, m):
            for j in range(0, n):
                if(obstacleGrid[i][j] == 1 or i == 0 and j == 0):
                    continue
                else:
                    a = 0
                    b = 0

                    if obstacleGrid[i-1][j] == 0:
                        a = grid[i-1][j]
                    
                    if obstacleGrid[i][j-1] == 0:
                        b = grid[i][j-1]

                    if(i == 0):
                        grid[i][j] = b
                    elif(j == 0):
                        grid[i][j] = a
        
        for i in range(1, m):
            for j in range(1, n):
                if(obstacleGrid[i][j] == 1):
                    continue
                else:
                    a = 0
                    b = 0

                    if obstacleGrid[i-1][j] == 0:
                        a = grid[i-1][j]
                    
                    if obstacleGrid[i][j-1] == 0:
                        b = grid[i][j-1]

                    grid[i][j] += (a+b)

        return grid[-1][-1]

                    
                    
                    


        
# @lc code=end



#
# @lcpr case=start
# [[0,0,0],[0,1,0],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,0]]\n
# @lcpr case=end

#

