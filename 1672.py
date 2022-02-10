class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Wealth1 = 0
        for i in range(len(accounts[0])):
            Wealth1 = Wealth1 + accounts[0][i]
        for j in range(1, len(accounts)):
            Wealth2 = 0
            for k in range(len(accounts[j])):
                Wealth2 = Wealth2 + accounts[j][k]
            if Wealth2 > Wealth1:
                Wealth1 = Wealth2
        return Wealth2
