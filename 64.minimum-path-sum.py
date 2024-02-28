#
# @lc app=leetcode id=64 lang=python3
# @lcpr version=30114
#
# [64] Minimum Path Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# TLE Recursive
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:

#         grid_m = len(grid)
#         grid_n = len(grid[0])

#         matrix=[] 
#         for i in range(grid_m): 
#             row=[] 
#             for j in range(grid_n): 
#                 row.append(-1) 
#             matrix.append(row) 
                
#         def solve(grid, y, x, cost):
#             if y > grid_m - 1 or x > grid_n - 1:
#                 return matrix
#             else:
#                 cost = cost + grid[y][x]
#                 if(matrix[y][x] == -1 or matrix[y][x] > cost):
#                     matrix[y][x] = cost
#             solve(grid, y+1, x, cost)
#             solve(grid, y, x+1, cost)

#         solve(grid, 0, 0, 0)

#         return matrix[-1][-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
        
# @lc code=end



#
# @lcpr case=start
# [[1,3,1],[1,5,1],[4,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#

