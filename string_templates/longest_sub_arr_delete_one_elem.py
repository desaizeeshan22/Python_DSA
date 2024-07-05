# 1493. Longest Subarray of 1's After Deleting One Element
# Medium
# Topics
# Companies
# Hint
# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Sliding Window (Shrinkable)
# state: cnt as the number of 0s in the window.
# invalid: cnt > 1 is invalid. if there are more than one zeros in the window it is invalid since
# we can only delete one element at most
def longestSubarray(nums):
    cnt = 0
    start, end = 0, 0
    max_len = 0
    while end < len(nums):
        cnt += nums[end] == 0
        while cnt > 1:
            cnt -= nums[start] == 0
            start += 1
        max_len = max(end - start,
                      max_len)  # note that the window is of size `end - start + 1`. We use `end - start` here because we need to delete a number aka 0.
        end += 1
    return max_len
    """
    :type nums: List[int]
    :rtype: int
    """


print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
