class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for idx in range(len(image)):
            image[idx] = list(reversed(image[idx]))
            image[idx] = [1 if b == 0 else 0 for b in image[idx]]
        return image
