class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]
        seen = set()
        self.floodFillHelper(image,sr,sc,newColor,starting_pixel,seen)
        return image
    
    def floodFillHelper(self,image,sr,sc,newColor,starting_pixel,seen):
        if  (sr >= 0 and sr < len(image)) and (sc>=0 and sc < len(image[sr])):
            coord =f'{sr},{sc}'
            if coord in seen:
                return
            if image[sr][sc]==starting_pixel:
                seen.add(coord)
                image[sr][sc]=newColor
                self.floodFillHelper(image,sr+1,sc,newColor,starting_pixel,seen) #up
                self.floodFillHelper(image,sr-1,sc,newColor,starting_pixel,seen) #down
                self.floodFillHelper(image,sr,sc+1,newColor,starting_pixel,seen) #right
                self.floodFillHelper(image,sr,sc-1,newColor,starting_pixel,seen) #left
            return 
            