#
# @lc app=leetcode id=347 lang=python3
# @lcpr version=30113
#
# [347] Top K Frequent Elements
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        counter = 0
        result = []
        for i, j in sorted(freq.items(),key=lambda x:x[1],reverse=True):
            result.append(i)
            counter += 1
            if(counter == k):
                return result
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

