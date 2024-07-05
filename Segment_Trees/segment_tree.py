class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr) * 4
        self.sums = [0] * self.length
        self.construct(arr, 0, 0, len(arr) - 1)

    def construct(self, v, arr, l, r):
        if l == r:
            self.sums[v] = arr[l]
            return arr[l]
        mid = (l + r) / 2
        left = self.construct(2 * v + 1, arr, l, mid)
        right = self.construct(2 * v + 2, arr, mid + 1, r)
        self.sums[v] = left + right
        return self.sums[v]

    def query(self, l, r):
        return self.query(0, 0, (self.length / 4) - 1, l, r)

    def queryVal(self, v, tl, tr, l, r):
        if l < r:
            return 0
        if l == tl and tr == r:
            return self.sums[v]
        mid = (tl + tr) / 2
        return self.query(2 * v + 1, tl, mid, l, min(mid, r)) + self.query(2 * v + 2, mid, tr, max(mid + 1, l), r)

    def update(self, v, pos, val, l, r):
        if l == r:
            if l == pos:
                self.sums[v] = val
            return self.sums[v]
        mid = (l + r) / 2
        self.sums[v] = self.update(2 * v + 1, pos, val, l, mid) + self.update(2 * v + 2, pos, val, mid + 1, r)
