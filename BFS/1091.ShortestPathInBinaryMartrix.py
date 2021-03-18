class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 标准bfs
        # BFS 一般通过队列方式来解决
        # 定义队列：用来存储被标记的节点

        # 判断边界条件 是否能直接返回结果
        if grid[0][0] == 1 or grid[-1][-1] == 1 or not grid:
            return -1

        queue = [(0, 0, 1)] # 将起始位置加入到队列中
        grid[0][0] = 1 # 同时更新备忘录
        # 备忘录：已经访问的位置
        # memo = []
        n = len(grid)
        if n == 1:
            return 1


        # BFS
        # 8 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]

        while(len(queue)>0):
            size = len(queue)
            for k in range(size):
                i, j, steps = queue.pop(0) # 取出第一个位置节点
                if i == n-1 and j == n-1: # 是否到达终点
                    return steps

                for dx, dy in directions: # 遍历接下来的所有节点
                    x, y= i+dx, j+dy

                    # 过滤不符合条件的位置
                    if 0 <= i+dx < n and 0<= j + dy < n:
                        if grid[x][y] == 0: # grid  直接作为memo， 如果没有访问过
                            queue.append((x, y, steps+1))
                            grid[x][y] = 1



        return -1