class Solution:
    def generateParenthesis(self, n: int):
        if n == 1:
            return ["()"]

        ans = []

        def help(n1, n2, res):
            """
            n1 number of remaining (
            n2 number of ramaining )
            """
            if n1 < 0 or n2 < 0:  # end
                return

            if n1 == 0 and n2 == 0:
                ans.append(res)
                return

            elif n1 > n2: # 3,2 // 3,1
                return

            elif n1 == n2:
                help(n1-1, n2, res+"(")
            else: # n1>n2
                help(n1, n2-1, res+")")
                help(n1 - 1, n2, res + "(")

            return

        help(n - 1, n, "(")

        print(ans)

s = Solution()
s.generateParenthesis(3)