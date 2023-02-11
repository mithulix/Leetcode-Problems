class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for a, b in redEdges:
            edges[a].append((b, "r"))
        for a, b in blueEdges:
            edges[a].append((b, "b"))

        ans = [-1] * n
        ans[0] = 0
        
        queue = deque([(0, 0, -1)])
        visit = {v: {"r":False, "b":False} for v in range(n)}
 
        while queue:
            v, dist, prev_colY = queue.popleft()
            for colX, colY in edges[v]:
                
                if colY != prev_colY and not visit[colX][colY]:
                    queue.append((colX, dist+1, colY))
                    visit[colX][colY] = True
                    
                    if -1 == ans[colX]:
                        ans[colX] = dist + 1
                    
        return ans