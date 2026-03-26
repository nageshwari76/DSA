class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=10**9+7
        adj = [[] for i in range(n)]
        for u,v,w  in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        dist = [float('inf')]*n
        ways =[0]*n
        dist[0]=0
        ways[0]=1
        pq = [(0,0)]
        while pq:
            d,node=heapq.heappop(pq)
            if d>dist[node]:
                continue
            for nei,wt in adj[node]:
                new=dist[node]+wt
                if new<dist[nei]:
                    dist[nei]=new
                    ways[nei]=ways[node]
                    heapq.heappush(pq,(new,nei))
                elif new==dist[nei]:
                    ways[nei]=(ways[nei]+ways[node]) %mod
        return ways[n-1]%mod







       
