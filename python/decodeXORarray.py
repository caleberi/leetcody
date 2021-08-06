class Solution:
    def decode(self, encoded: list, first: int) -> list:
        if first is None:
            return []
        decodedArray = [first]
        for idx, encodedBit in enumerate(encoded):
            decodedArray.append(decodedArray[-1] ^ encodedBit)
        return decodedArray
