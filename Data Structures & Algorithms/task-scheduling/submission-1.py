class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        organized = [-freq for task, freq in counts.items()]
            
        heapq.heapify(organized)

        totalTime = 0
        
        while organized or used:
            completed = 0
            used = []

            for i in range(n+1):
                if organized:
                    nextTask = heapq.heappop(organized)

                    nextTask += 1
                    completed += 1

                    if nextTask < 0:
                        used.append(nextTask)
            
            for freq in used:
                heapq.heappush(organized, freq)
            
            if organized: # need to figure out how to calculate cycles
                totalTime += n + 1
                
            else:
                totalTime += completed
            

        return totalTime
            

