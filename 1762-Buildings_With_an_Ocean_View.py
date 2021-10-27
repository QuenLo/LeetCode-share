class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        max_height = 0
        len_building = len(heights)-1
        ans_list = []
        for ind, height in enumerate(heights[::-1]):
            
            if height > max_height:
                ans_list.append( len_building - ind )
                max_height = height
                
        return ans_list[::-1]
