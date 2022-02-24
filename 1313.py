class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(int(len(nums)/2)):
            freq = nums[2*i]
            val = nums[2*i+1]
            for j in range(freq):
                result.append(val)
        return result
