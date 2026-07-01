class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            n = numbers[left] + numbers[right]

            if target < n:
                right -= 1
            elif target > n:
                left += 1
            else:
                return [left+1, right+1]
        
        return []