#
# @lc app=leetcode id=4 lang=python3
# @lcpr version=30113
#
# [4] Median of Two Sorted Arrays
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1_len = len(nums1)
        nums2_len = len(nums2)
        length = nums1_len + nums2_len

        nums1_idx = 0
        nums2_idx = 0

        # nums1_middle_idx = int((nums1_len + 1) / 2) - 1
        # nums2_middle_idx = int((nums2_len + 1) / 2) - 1

        # if(nums1_middle_idx)

        if(length % 2 == 1):
            if(nums1[0] < nums2[0]):
                while nums1_idx + nums2_idx < int(length / 2):
                    if(nums1[nums1_idx] <= nums2[nums2_idx]):
                        if(nums1_idx < nums1_len - 1):
                            nums1_idx +=1
                        else:
                            if(nums2_idx < nums2_len - 1):
                                nums2_idx +=1
                    else:
                        if(nums2_idx < nums2_len - 1):
                            nums2_idx +=1
                        else:
                            if(nums1_idx < nums1_len - 1):
                                nums1_idx +=1

                    if(nums1_idx + nums2_idx == int(length / 2)):
                        if(nums1[nums1_idx] > nums2[nums2_idx]):
                            return nums2[nums2_idx]
                        else:
                            return nums1[nums1_idx]
            else:
                while nums1_idx + nums2_idx < int(length / 2):
                    if(nums1[nums1_idx] >= nums2[nums2_idx]):
                        if(nums2_idx < nums2_len - 1):
                            nums2_idx +=1
                        else:
                            if(nums1_idx < nums1_len - 1):
                                nums1_idx +=1
                    else:
                        if(nums1_idx < nums1_len - 1):
                            nums1_idx +=1
                        else:
                            if(nums2_idx < nums2_len - 1):
                                nums2_idx +=1

                    if(nums1_idx + nums2_idx == int(length / 2)):
                        if(nums1[nums1_idx] > nums2[nums2_idx]):
                            return nums2[nums2_idx]
                        else:
                            return nums1[nums1_idx]
        else:
            return 0
        
# @lc code=end



#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#

