#
# @lc app=leetcode id=119 lang=python3
# @lcpr version=30114
#
# [119] Pascal's Triangle II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        result = []

        rowIndex +=1

        for row in range(1,rowIndex+1,1):
            
            temp_row = []

            for i in range(0, row, 1):

                if i == 0 or i == row-1:
                    temp_row.append(1)
                else:
                    last_row = result
                    temp_row.append(last_row[i] + last_row[i-1])

            result = temp_row

        return result

        
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

