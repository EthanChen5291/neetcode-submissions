class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        # max num of dual fruit

        # two most common

        left = 0

        maxFruit = 1
        fruitMap = {}

        for right in range(len(fruits)):
            fruitMap[fruits[right]] = fruitMap.get(fruits[right], 0) + 1

            while len(fruitMap) > 2:
                fruitMap[fruits[left]] -= 1

                if fruitMap[fruits[left]] == 0:
                    del fruitMap[fruits[left]]
                
                left += 1

            maxFruit = max(right - left + 1, maxFruit)
        
        return maxFruit



