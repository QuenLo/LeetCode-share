class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car_pool = [0]*1001
        for pa, start, end in trips:
            car_pool[start] += pa
            car_pool[end] -= pa
        now_pa = 0
        for stop in car_pool:
            now_pa += stop
            if now_pa > capacity:
                return False
            
        return True
        
# Sort the pickup and dropoff events by location, then process them in order.
class SolutionII:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car_pool = []
        for pa, start, end in trips:
            car_pool.extend( [(start, pa), (end, -pa)] )
            
        now_pa = 0
        for _, stop in sorted(car_pool):
            now_pa += stop
            if now_pa > capacity:
                return False
            
        return True
