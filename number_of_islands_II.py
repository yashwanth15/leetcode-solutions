class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False   # no merge happened

        # union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True   # merge happened

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind()
        land = set()
        results = []
        count = 0   # number of islands
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        for r, c in positions:

            # if land already added
            if (r, c) in land:
                results.append(count)
                continue

            land.add((r, c))
            id1 = r * n + c
            uf.add(id1)
            count += 1

            # try merging with neighbors
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr, nc) in land:
                    id2 = nr * n + nc
                    uf.add(id2)

                    if uf.union(id1, id2):
                        count -= 1   # two islands merged

            results.append(count)

        return results
