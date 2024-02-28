#
# @lc app=leetcode id=118 lang=python3
# @lcpr version=30114
#
# [118] Pascal's Triangle
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []

        for row in range(1,numRows+1,1):
            
            temp_row = []

            for i in range(0, row, 1):

                if i == 0 or i == row-1:
                    temp_row.append(1)
                else:
                    last_row = result[-1]
                    temp_row.append(last_row[i] + last_row[i-1])

            result.append(temp_row)

        return result

        
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

