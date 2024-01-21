#
# @lc app=leetcode id=74 lang=python3
# @lcpr version=30113
#
# [74] Search a 2D Matrix
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_start_idx = 0
        row_end_idx = len(matrix) - 1
        column_start_idx = 0
        column_end_idx = len(matrix[0]) - 1

        if target < matrix[0][0] or target > matrix[row_end_idx][column_end_idx]:
            return False
        
        if target == matrix[0][0] or target == matrix[row_end_idx][column_end_idx]:
            return True
    
        while(1):
            
            diff = (column_start_idx + ((row_end_idx - row_start_idx) * len(matrix[0]) + (column_end_idx - column_start_idx)) // 2)
            row_mid_idx =  row_start_idx + (diff) // len(matrix[0])
            column_mid_idx = diff % len(matrix[0])

            if target == matrix[row_start_idx][column_start_idx]:
                return True
            
            if target == matrix[row_end_idx][column_end_idx]:
                return True

            print('start:',row_start_idx, column_start_idx)
            print('end:',row_end_idx, column_end_idx)
            print('mid:',row_mid_idx, column_mid_idx)

            if matrix[row_mid_idx][column_mid_idx] <= matrix[row_start_idx][column_start_idx]:
                return False
            
            if matrix[row_mid_idx][column_mid_idx] >= matrix[row_end_idx][column_end_idx]:
                return False
            
            # if(matrix[row_start_idx][column_start_idx] == matrix[row_mid_idx][column_mid_idx]):
            #     return False
            
            # if(matrix[row_end_idx][column_end_idx] == matrix[row_mid_idx][column_mid_idx]):
            #     return False


            if(matrix[row_mid_idx][column_mid_idx] < target):
                row_start_idx = row_mid_idx
                column_start_idx = column_mid_idx
            elif(matrix[row_mid_idx][column_mid_idx] > target):
                row_end_idx = row_mid_idx
                column_end_idx = column_mid_idx
            else:
                return True
            


            
            
            
            


            

        #print(row_end_idx,column_end_idx)

# @lc code=end

# [[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n7\n

# [[ 1, 3, 5 ,7]
# ,[10,11,16,20]
# ,[23,30,34,50]]\n7\n

#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#

