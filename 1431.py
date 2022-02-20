class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = 0
        greatestcandies = []
        for i in range(len(candies)):
            if candies[i] > maxcandies:
                maxcandies = candies[i]
            for j in range(len(candies)):
                pluscandies = candies[i] + extraCandies
            if pluscandies >= maxcandies:
                greatestcandies.append(True)
            else:
                greatestcandies.append(False)
        return greatestcandies
