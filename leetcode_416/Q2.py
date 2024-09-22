class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def is_possible(mountainHeight, maxTime, workerTimes):
            reduction = 0
            for time in workerTimes:
                lo = 1
                hi = mountainHeight
                while lo <= hi:
                    mid = (lo + hi) // 2
                    cost = (mid * (mid + 1)) / 2
                    cost = time * cost
                    if cost <= maxTime:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                reduction += hi
                if reduction >= mountainHeight:
                    return True
            return reduction >= mountainHeight

        lo = 1
        hi = int(1e18)
        res = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mountainHeight, mid, workerTimes):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res

        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
