#
# @lc app=leetcode id=480 lang=python3
# @lcpr version=30113
#
# [480] Sliding Window Median
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from bisect import bisect, bisect_left
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        start = 0
        end = k
        result = []
        sliding_window = []

        sliding_window = nums[start:end]
        sliding_window.sort()

        mid = len(sliding_window) // 2

        if(k % 2 == 1):
            result.append(sliding_window[mid])
        else:
            result.append((sliding_window[mid - 1] + sliding_window[mid]) / 2)

        start += 1
        end   += 1

        while(end < len(nums) + 1):
            previous = nums[start - 1]
            next = nums[end - 1]

            del sliding_window[bisect_left(sliding_window, previous)]
            insort(sliding_window, next)

            mid = len(sliding_window) // 2

            if(k % 2 == 1):
                result.append(sliding_window[mid])
                
            else:
                result.append((sliding_window[mid - 1] + sliding_window[mid]) / 2)

            start += 1
            end   += 1

        return result
        
# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,2,3,1,4,2]\n3\n
# @lcpr case=end

#

