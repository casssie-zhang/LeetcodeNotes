class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)
        if len(arr) == 2:
            return 1 if arr[0] == arr[1] else 2

        dp = [2 for i in arr]
        inc = arr[0] > arr[1]  # next stage is increase
        ans = 0
        for i in range(2, len(arr)):
            if inc and arr[i] > arr[i - 1]:
                dp[i] = dp[i - 1] + 1
                inc = False
            elif not inc and arr[i] < arr[i - 1]:
                dp[i] = dp[i - 1] + 1
                inc = True
            else:
                if arr[i] == arr[i - 1]:
                    dp[i] = 1
                else:
                    inc = arr[i] < arr[i - 1]
                    dp[i] = 2
            ans = max(dp[i], ans)
            # print(dp)
        return ans
