#
# @lc app=leetcode id=234 lang=python3
# @lcpr version=30114
#
# [234] Palindrome Linked List
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import copy
 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        list = []

        def reverse(h):
            if h.next is None:
                list.append(h.val)
                return h
            
            list.append(h.val)

            new_list = reverse(h.next)

            front = h.next
            h.next = None
            front.next = h

            return new_list
        
        reversed = reverse(copy(head))

        idx = 0 

        while reversed.next is not None:
            #print(head.val,reversed.val)
            if(list[idx]!= reversed.val):
                return False
            idx += 1
            reversed = reversed.next

        return True



# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

