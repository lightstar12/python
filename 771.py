class Solution:
  def nuJewelsInStones(self, jewels: str, stones: str) -> int:
    jewels_ = 0
    for i in range(len(jewels)):
      for j in range(len(stones)):
        if jewels[i] == stones[j]:
          jewels_ = jewels_ + 1
    retrun jewels_
