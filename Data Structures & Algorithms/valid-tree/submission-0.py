class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(n)}
        visit = set()


        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(src, prev):
            if src in visit:
                return False

            visit.add(src)

            for nei in adj[src]:
                if nei == prev:
                    continue

                if not dfs(nei, src):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n