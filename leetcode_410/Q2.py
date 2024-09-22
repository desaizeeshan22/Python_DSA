class Solution(object):
    def countGoodNodes(self, edges):
        self.construct(edges)
        n = len(edges)
        self.visited = [False] * (n + 1)
        is_good = [False] * (n + 1)
        for i in range(n + 1):
            if not self.visited[i]:
                self.height(0, is_good)
        res = 0
        for elem in is_good:
            res += (elem == True)
        return res

    def construct(self, edges):
        self.adj_list = dict()
        for i in range(len(edges) + 1):
            self.adj_list[i] = []
        for edge in edges:
            self.adj_list[edge[0]].append(edge[1])
            self.adj_list[edge[1]].append(edge[0])

    def height(self, node, is_good):
        heights = set()
        temp = 0
        self.visited[node] = True
        for n in self.adj_list[node]:
            if not self.visited[n]:
                h = self.height(n, is_good)
                temp += h
                heights.add(h)
        if len(heights) == 1 or len(heights) == 0:
            is_good[node] = True
        return 1 + temp

        """
        :type edges: List[List[int]]
        :rtype: int
        """
