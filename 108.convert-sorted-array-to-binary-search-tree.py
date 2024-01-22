#
# @lc app=leetcode id=108 lang=python3
# @lcpr version=30113
#
# [108] Convert Sorted Array to Binary Search Tree
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        length = len(nums)
        mid_idx = (length) // 2
        
        if length == 0:
            return None

        return TreeNode(
            nums[mid_idx],
            self.sortedArrayToBST(nums[:mid_idx]),
            self.sortedArrayToBST(nums[mid_idx+1:])
        )



        



        

        
# @lc code=end



#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#

