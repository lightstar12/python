class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s_num = []
        for i in range(len(nums)):
            ss_num = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] > nums[j]:
                    ss_num = ss_num + 1
            s_num.append(ss_num)
        return s_num
