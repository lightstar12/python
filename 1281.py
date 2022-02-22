class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prodigi = 1
        sumdigi = 0
        n_str = str(n)
        for i in range(len(n_str)):
            prodigi = prodigi * int(n_str[i])
            sumdigi = sumdigi + int(n_str[i])
        result = prodigi - sumdigi
        if result < 0:  return -result
        else:   return result
