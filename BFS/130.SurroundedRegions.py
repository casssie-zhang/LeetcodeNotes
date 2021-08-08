class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = []
        h = len(board)
        w = len(board[0])

        for i in range(h):
            for j in range(w):
                if (i == 0 or j == 0 or i == h - 1 or j == w - 1) and board[i][j] == "O":
                    queue.append((i, j))

        while queue:
            i, j = queue.pop(0)
            board[i][j] = "T"

            for dx, dy in directions:
                if 0 <= i + dx < h and 0 <= j + dy < w:
                    if board[i + dx][j + dy] == "O":
                        queue.append((i + dx, j + dy))

        # print(board)
        for i in range(h):
            for j in range(w):

                if board[i][j] == "O":
                    board[i][j] = "X"

                if board[i][j] == "T":
                    board[i][j] = "O"
