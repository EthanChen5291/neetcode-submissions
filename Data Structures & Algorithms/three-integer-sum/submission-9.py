class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)

        left = 0
        right = len(sortedNums) - 1

        res = []

        for i in range(len(sortedNums)):
            target = -(sortedNums[i])
            print(target)

            if sortedNums[i] > 0:
                break

            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue

            left = i+1
            right = len(sortedNums) - 1

            while left < right:
                leftNum = sortedNums[left]
                rightNum = sortedNums[right]

                if leftNum + rightNum == target:
                    res.append([leftNum, rightNum, -target])
                    
                    while left < right and sortedNums[left] == sortedNums[left + 1]:
                        left += 1
                    while left < right and sortedNums[right] == sortedNums[right - 1]:
                        right -= 1
                    
                    right -= 1
                    left += 1

                elif leftNum + rightNum < target:
                    left += 1
                elif leftNum + rightNum > target:
                    right -= 1

        return res