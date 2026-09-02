class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [sorted]

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if target == total:
                return [left+1, right+1]
            elif target < total:
                right -= 1
            else:
                left += 1
        

