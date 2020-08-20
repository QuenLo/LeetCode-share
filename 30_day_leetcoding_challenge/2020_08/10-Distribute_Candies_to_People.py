class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        ans_candy = [0]*num_people
        give = 1
        
        while candies >= give:
            ans_candy[ give%num_people -1 ] += give
            candies -= give
            give +=1
        
        ans_candy[ give%num_people -1 ] += candies
        
        return ans_candy
