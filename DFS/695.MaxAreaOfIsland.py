class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # height and width
        self.h = len(grid)
        self.w = len(grid[0])

        self.grid = grid
        self.visit = [[0 for j in range(self.w)] for i in range(self.h)] # save nodes that have been visited
        ans = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.visit[i][j] == 1: # if this node has been visited, ignore
                    continue
                else:
                    self.visit[i][j] == 1
                if grid[i][j] == 1:
                    cnt = self.dfs(i, j)
                    ans = max(ans, cnt)

        return ans

    def dfs(self, i, j):
        """i, j is the starting point of dfs"""

        if i >= self.h or i < 0 or j >= self.w or j < 0: # border
            return 0

        if self.grid[i][j] == 0 or self.visit[i][j]==1: # if is zero or has been visited, should not be counted
            return 0

        # connected
        self.visit[i][j] = 1
        return 1 + self.dfs(i+1, j) + self.dfs(i, j+1) + \
        self.dfs(i-1, j) + self.dfs(i, j-1)
