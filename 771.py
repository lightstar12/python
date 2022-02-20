class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_ = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    jewels_ = jewels_ + 1
        return jewels_
