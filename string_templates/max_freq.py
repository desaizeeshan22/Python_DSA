#1838. Frequency of the Most Frequent Element
#Solved
#Medium
#Topics
#Companies
#Hint
#The frequency of an element is the number of times it occurs in an array.

#You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

#Return the maximum possible frequency of an element after performing at most k operations.
Sort the input array in ascending order

#In order to maximize the frequency of an element , since the operations involve incrementing values
we can increment all the elements lesser than the current element, the sum of the differences
between the current running sum upto the element and the case where all the elements
before and including the current element were equal to the current element forms the number of operations
required to make all the elements within the current window equal to the current element
which maximizes the frequency.


#If these number of operations <=k we set the frequency of the element as the window size since
after these operations the number of elements equal to the current element would have been equal to the current
window size
#For example, assume the window is [1,2,3], increasing all the numbers to 3 will take 3 * 3 - (1 + 2 + 3) operations.
#If the window is invalid aka the number of operations is >k remove the element of the slow pointer from the running
sum and shrink the window till it becomes valid

def maxFrequency(nums, k):
        nums.sort()
        slow,fast=0,0
        running_sum=0
        max_freq=0
        while fast<len(nums):
            running_sum+=nums[fast]
            while (fast-slow+1)*nums[fast]-running_sum>k:
                running_sum-=nums[slow]
                slow+=1
            max_freq=max(fast-slow+1,max_freq)
            fast+=1
        return max_freq
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
print(maxFrequency([1,4,8,13],5))