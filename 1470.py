class Solution:
    def shuffle(self, nums:List[int], n: int) -> List[int]:
        numss = []
        for i in range(n):
            numss.append(nums[i])
            numss.append(nums[n+i])
        return numss
