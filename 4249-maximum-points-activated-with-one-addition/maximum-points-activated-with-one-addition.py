class Solution:
    def maxActivated(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        size = [1] * n

        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i
                parent[root_j] = root_i
                size[root_i] += size[root_j]

        xmap, ymap = {}, {}
        for i, (x, y) in enumerate(points):
            if x in xmap: union(i, xmap[x])
            else: xmap[x] = i
            if y in ymap: union(i, ymap[y])
            else: ymap[y] = i

        sizes = [size[i] for i in range(n) if parent[i] == i]
        sizes.sort(reverse=True)
        
        m1 = sizes[0] if len(sizes) > 0 else 0
        m2 = sizes[1] if len(sizes) > 1 else 0
        return m1 + m2 + 1