class Solution:
    def countBits(self, num: int) -> List[int]:
        # brute force:
        # TODO: bin(Int).count("1")
        # res = []
        # for i in range(num+1):
        #     res.append(bin(i).count("1"))
        # return res

        # solution2: recursion
        # 偶数

    #     res = []
    #     for i in range(num + 1):
    #         res.append(self.count(i))
    #     return res

    # def count(self, num):
    #     if num == 0:
    #         return 0
    #     elif num % 2 == 0:
    #         return self.count(num // 2)
    #     else:
    #         return 1 + self.count((num - 1) // 2)

        self.res = []
        for i in range(num + 1):
            self.res.append(self.count(i))
        return self.res

    def count(self, num):
        # recursion fn
        if num == 0:
            return 0
        elif num % 2 == 0:
            return self.res[num // 2]
        else:
            return 1 + self.res[(num - 1) // 2]

