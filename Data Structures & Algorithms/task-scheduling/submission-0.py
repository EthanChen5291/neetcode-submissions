class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # separate tasks into task types
        # go along the types, doing 1 per type
        # if len(types) < n, add n - len(types) cpu cycles to the iteration

        count = Counter(tasks)

        heap = [-freq for freq in count.values()]
        heapq.heapify(tasks)

        time = 0

        while heap:
            used = []

            for i in range(n+1):
                if heap:
                    freq = heapq.heappop(heap)
                    freq += 1
                    
                    time += 1
                    
                    if freq < 0:
                        used.append(freq)
                
                elif used:
                    time += 1
                else:
                    break
            
            for freq in used:
                heapq.heappush(heap, freq)
        
        return time
                    

