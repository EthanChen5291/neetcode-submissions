class LRUCache:

    def __init__(self, capacity: int):
        self.items = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        
        value = self.items.pop(key)
        self.items[key] = value
        return value  

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            del self.items[key]
        
        self.items[key] = value

        if len(self.items) > self.capacity:
            del self.items[next(iter(self.items))]
        
        return
            # remove least recently used


        
