class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        # TODO: 方法2 记数组的长度为 n，由于只能从开头和末尾拿 k 牌，所以最后剩下的必然是连续的 n-k

        cardPoints = cardPoints[-k:] + cardPoints[:k]
        # print("LENGTH:", len(cardPoints), cardPoints)
        i=0
        prev = sum(cardPoints[:k])
        ans=prev

        start=cardPoints[0]

        # print(cardPoints, prev, start)
        while(i<k):
            tmp = prev-start+cardPoints[i+k]
            ans = max(ans, tmp)
            prev = prev-start+cardPoints[i+k] # 更新prev
            start = cardPoints[i+1] # 更新start

            # print(i, i+k, ans, start)
            i += 1

        return ans