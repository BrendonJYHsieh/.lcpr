#
# @lc app=leetcode id=451 lang=python3
# @lcpr version=30113
#
# [451] Sort Characters By Frequency
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# class Solution:
#     def frequencySort(self, s: str) -> str:

#         table = {}

#         for c in s:
#             if(not table.get(c)):
#                 table[c] = c
#             else:
#                 table[c] += c 

#         result = ''
#         symbol = ''
        
#         while len(result) != len(s):
#             max = 0
#             for k, v in table.items():
#                 if(len(v) > max):
#                     max = len(v)
#                     symbol = k
                
#             result += table[symbol]
#             table[symbol] = ''
        
#         return result
class Solution:
    def frequencySort(self, s: str) -> str:

        table = {}
        count_table = {}
        result = ''

        for c in s:
            if(not table.get(c)):
                table[c] = c
            else:
                table[c] += c 

        for k, v in table.items():
            length = len(v)
            if(length not in count_table.keys()):
                count_table[length] = k
            else:
                count_table[length] += k

        length = len(count_table.keys())

        for idx in range(0, length, 1):
            max_key = max(count_table.keys())
            for item in count_table[max_key]:
                for i in range(0, max_key, 1):
                    result +=item
                print(item)
            del count_table[max_key]
        return result

        
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         freq=Counter(s)
#         ans=''
#         for i,j in sorted(freq.items(),key=lambda x:x[1],reverse=True):
#             ans=ans+i*j
#         return ans
# @lc code=end



#
# @lcpr case=start
# "tree"\n
# @lcpr case=end

# @lcpr case=start
# "cccaaa"\n
# @lcpr case=end

# @lcpr case=start
# "Aabb"\n
# @lcpr case=end

#

