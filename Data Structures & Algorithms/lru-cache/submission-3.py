class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        val = self.cache.pop(key)
        self.cache[key] = val
        
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        
        self.cache[key] = value
    
        if len(self.cache) > self.capacity:
            del self.cache[next(iter(self.cache))]


        


        
