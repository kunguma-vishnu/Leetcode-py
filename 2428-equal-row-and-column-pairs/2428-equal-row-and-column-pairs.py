class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        cnt = 0
        for row in grid:
            d[str(row)] += 1
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            cnt += d[str(col)]
        return cnt
