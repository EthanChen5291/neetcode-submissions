class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)

        left = 0
        right = len(sortedNums) - 1

        res = []

        for i in range(len(sortedNums)):
            target = -(sortedNums[i])
            print(target)

            left = i+1
            right = len(sortedNums) - 1

            while left < right:
                #print(f'left: {left}, right: {right}')

                leftNum = sortedNums[left]
                rightNum = sortedNums[right]

                if leftNum + rightNum == target:
                    if [leftNum, rightNum, -target] not in res:
                        res.append([leftNum, rightNum, -target])
                    
                    if left+1 <= right:
                        left += 1
                    elif right+1 < len(sortedNums):
                        right += 1
                    else:
                        break

                elif leftNum + rightNum < target:
                    left += 1
                elif leftNum + rightNum > target:
                    right -= 1

        return res