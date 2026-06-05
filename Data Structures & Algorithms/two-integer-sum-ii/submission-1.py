class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i1, n in enumerate(numbers):
            val = target - n
            if val in numbers:
                i2 = numbers.index(val)
                print(f"{i1}, {i2}")
                return([min(i1 + 1, i2 + 1), max(i1 + 1, i2 + 1)])