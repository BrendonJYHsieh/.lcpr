#
# @lc app=leetcode id=3 lang=python3
# @lcpr version=30113
#
# [3] Longest Substring Without Repeating Characters
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # container = []

        # max = 0
        # idx = 0
        # length = len(s)
        # while idx < length:
        #     if s[idx] in container:
        #         container = []
        #         for temp in range(idx - 1, -1, -1):
        #             if(s[temp] == s[idx]):
        #                 idx = temp + 1
        #                 break
            
        #     container.append(s[idx])

        #     if(len(container) > max):
        #         max = len(container)
        #     idx +=1
        # return max

        table = {}
        start = 0
        result = 0

        for idx, letter in enumerate(s):

            if(table.get(letter, -1) >= start):
                start = table[letter] + 1

            result = max(result, idx - start + 1)
            table[letter] = idx

        return result


        
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

