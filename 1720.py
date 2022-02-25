class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decod = [first]
        decod_2 = first^encoded[0]
        decod.append(decod_2)
        for i in range(1,len(encoded)):
            decod_2 = decod_2^encoded[i]
            decod.append(decod_2)
        return decod
