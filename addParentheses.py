class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in '+-*':
                print(f"@{i}:")
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                print(left, right)

                for l in left:
                    for r in right:
                        print(f'{l}{char}{r}')
                        res.append(eval(f'{l}{char}{r}'))
        return res


if __name__ == '__main__':
    inputs = "2*3-4*5"
    s = Solution()
    print(s.diffWaysToCompute(inputs))