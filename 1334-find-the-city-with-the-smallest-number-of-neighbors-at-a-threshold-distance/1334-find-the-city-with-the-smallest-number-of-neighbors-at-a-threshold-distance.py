class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[float('inf')]*n for i in range(n)]
        for i in range(n):
            dist[i][i]=0
        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != float('inf')and dist[via][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j])
        minc=float('inf')
        city=-1
        for i in range(n):
            count=0
            for j in range(n):
                if dist[i][j]<=distanceThreshold:
                    count+=1
            if count<=minc:
                minc=count
                city=i
        return city