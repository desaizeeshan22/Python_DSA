class Solution(object):
    def countPairs(self, nums):
        res = 0
        d = dict()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if self.is_possible(nums[i], nums[j]):
                    res += 1
        return res

    def is_possible(self, n1, n2):
        s1 = str(n1)
        s2 = str(n2)
        max_length = max(len(s1), len(s2))
        s1 = s1.zfill(max_length)
        s2 = s2.zfill(max_length)

        diff_count = 0
        diff_index = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_count += 1
                diff_index.append(i)
                if diff_count > 2:
                    return False

        if diff_count == 0:
            return True
        if diff_count == 2:
            idx1, idx2 = diff_index
            s1_list = list(s1)
            s1_list[idx1], s1_list[idx2] = s1_list[idx2], s1_list[idx1]

            return ''.join(s1_list) == s2

        return False

