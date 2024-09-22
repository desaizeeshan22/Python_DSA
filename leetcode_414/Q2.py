# class Solution(object):
#     def maxPossibleScore(self, start, d):
#         print(self.is_possible(2, start))

def is_possibe(diff, start, d):
    initial_val = start[0]
    for i in range(1, len(start)):
        temp = initial_val + diff
        if temp >= start[i] or temp <= start[i] + d:
            initial_val = temp
        elif temp < start[i]:
            initial_val = start[i]
        else:
            return False
    return True


"""
:type start: List[int]
:type d: int
:rtype: int
"""
print(is_possibe(4, [0, 3, 6], 2))
