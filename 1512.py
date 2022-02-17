class Solution:
  def numIdenticalPairs(self, nums: List[int]) -> int:
    pairs = 0
    for i in range(len(nums)):
      for j in range(i, len(nums)):
        if nums[i] == nums[j]:
          pairs = pairs + 1
    return pairs
