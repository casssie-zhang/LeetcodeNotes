"""void BFS()
{
    定义队列;
    定义备忘录，用于记录已经访问的位置；

    判断边界条件，是否能直接返回结果的。

    将起始位置加入到队列中，同时更新备忘录。

    while (队列不为空) {
        获取当前队列中的元素个数。
        for (元素个数) {
            取出一个位置节点。
            判断是否到达终点位置。
            获取它对应的下一个所有的节点。
            条件判断，过滤掉不符合条件的位置。
            新位置重新加入队列。
        }
    }

}

作者：hank-36
链接：https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/solution/biao-zhun-de-bfsjie-fa-duo-lian-xi-jiu-hui-zhang-w/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
}"""



class Solution(object):

    def shortestPathBinaryMatrix_standard(self, grid):
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


    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS 一般通过队列方式来解决
        # 定义队列：用来存储被标记的节点

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
            i, j, steps = queue.pop(0) # 取出一个位置节点

            for dx, dy in directions: # 遍历方向
                x, y= i+dx, j+dy
                if x == n - 1 and y == n - 1:  # 判断(下一个节点）是否到达终点位置
                    return steps+1

                if 0 <= i+dx < n and 0<= j + dy < n:
                    if grid[x][y] == 0: # grid  直接作为memo， 如果没有访问过
                        queue.append((x, y, steps+1)) # 新位置加入队列
                        grid[x][y] = 1



        return -1



if __name__ == '__main__':
    s = Solution()
    inputs = [[0,0,0],[1,1,0],[1,1,1]]
    print(s.shortestPathBinaryMatrix(inputs))
    print(s.shortestPathBinaryMatrix_standard(inputs))


    inputs=[[0]]
    print(s.shortestPathBinaryMatrix(inputs))
    print(s.shortestPathBinaryMatrix_standard(inputs))
