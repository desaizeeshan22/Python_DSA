from collections import defaultdict


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    counter = len(t)
    d = defaultdict(int)
    # count and initialize every character in the substring t
    for char in t:
        d[char] += 1
    # initialize two pointers start and end
    # to assess a window, start and end vars  mark the beginning and end of the window respectively
    start = 0
    end = 0
    min_length = float("inf")
    # variable to store the start of the minimum window substring
    min_start = 0
    while (end < len(s)):
        # if you find a character in s which is present in substring t
        # reduce counter by 1 aka window contains one of the characters
        # aka the character has been included in the window
        if (d[s[end]] > 0):
            counter -= 1
        # reduce the frequency of the character by 1
        d[s[end]] -= 1
        end += 1
        # if all the characters from the substring have been included in a window of the main string s
        # check and calculate minimum length of the substring window
        while counter == 0:
            if end - start < min_length:
                # update the minimum length of the substring window and the starting index of the substring
                min_length = end - start
                min_start = start
            # increment counter by 1 marking the frequency aka number of times the character needs to be
            # visited in the updated substring window
            d[s[start]] += 1
            # if a character is a part of the substring t increment the counter by 1 which invalidatea the current window
            if d[s[start]] > 0:
                counter += 1
            # increment the starting position by one to shrink the window
            start += 1
    if min_length == float("inf"):
        return ""
    return s[min_start:min_start + min_length]


print(minWindow("ADOBECODEBANC", "ABC"))
