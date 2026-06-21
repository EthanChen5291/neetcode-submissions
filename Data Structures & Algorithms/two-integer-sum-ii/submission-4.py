class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            print(f'left: {left}, right: {right}')
            sumNums = numbers[left] + numbers[right]

            if target > sumNums:
                left += 1
            elif target == sumNums:
                if numbers[left] != numbers[right]:
                    return [left + 1, right + 1]
            else:
                right -= 1
        
        return []
                