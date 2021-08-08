import math

class Solution:
    def numSquares(self, n: int) -> int:
        import math
        # res = self.dfs(n, 0, n)
        res = self.bfs(n)

        return res

    def bfs(self, n):
        queue = [(n, 0)]
        visited = set()
        while (queue):
            # print(queue)
            tmp, step = queue.pop(0)
            start = int(math.sqrt(tmp))
            # print("start:", start)
            candidates = [tmp - i * i for i in range(1, start + 1)]
            # print("tmp:", tmp, "step:", step, "candidates:", candidates)
            for i in candidates:
                if i in visited:
                    continue
                if i == 0:
                    return step + 1
                queue.append((i, step + 1))
                visited.add(i)
            # print(queue)

        return

        # def dfs(self, diff, step, begin):
    #     # 超出时间限制
    #     if diff == 0:
    #         # print("find Solution: ",step)
    #         return step

    #     start = int(math.sqrt(diff))
    #     start = min(start, begin)

    #     # print(diff, "steps:", step, "start=",start, "begin=",begin)
    #     ans = 10000
    #     while(start > 0):
    #         # print("next:", diff-start*start)
    #         res = self.dfs(diff-start*start, step+1, start)
    #         ans = min(ans, res)
    #         start -= 1
    #     return ans