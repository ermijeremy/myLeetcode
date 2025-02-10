class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = list(reversed(image[i]))
            image[i] = list(map(int, ''.join((map(str, image[i]))).replace("0","a").replace("1","0").replace("a","1")))
        return image