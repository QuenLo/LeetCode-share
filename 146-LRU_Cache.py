from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Cache = OrderedDict()
        

    def get(self, key: int) -> int:
        
        if key in self.Cache:
            self.Cache.move_to_end(key)
            return  self.Cache[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.Cache:
             self.Cache.move_to_end(key)
        self.Cache[key] = value
        if len( self.Cache ) > self.capacity:
             self.Cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
