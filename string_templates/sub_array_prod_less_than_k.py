# 713.
# Subarray
# Product
# Less
# Than
# K
# Solved
# Medium
# Topics
# Companies
# Hint
# Given
# an
# array
# of
# integers
# nums and an
# integer
# k,
# return the
# number
# of
# contiguous
# subarrays
# where
# the
# product
# of
# all
# the
# elements in the
# subarray is strictly
# less
# than
# k.
#
# Example
# 1:
#
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The
# 8
# subarrays
# that
# have
# product
# less
# than
# 100
# are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note
# that[10, 5, 2] is not included as the
# product
# of
# 100 is not strictly
# less
# than
# k.
# Example
# 2:
#
# Input: nums = [1, 2, 3], k = 0
# Output: 0
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106

# Calculate running product
# We have a window initialized by start and end pointers
# If the product in the window is strictly  less than k
# add number of subarrays which is given by end-start+1
# If the window is invalid then shrink the window by incrementing the start pointer and removing the
# element at the start pointer by dividing the running product by the element value
##Invalid conditions if running_product >=k and start<=end so that start does not go out of bounds
def numSubarrayProductLessThanK(nums, k):
    prod = 1
    end, start = 0, 0
    res = 0
    n = len(nums)
    while end < n:
        prod *= nums[end]
        while prod >= k and start <= end:
            prod /= nums[start]
            start += 1
        res += (end - start + 1)
        end += 1
    return res
