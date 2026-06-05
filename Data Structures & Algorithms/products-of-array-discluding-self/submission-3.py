class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_zeros = True
        zerosCount = 0
        
        for n in nums:
            if n != 0:
                all_zeros = False
            else:
                zerosCount += 1
        
        print(zerosCount)

        if all_zeros:
            return nums
        
        if zerosCount >= 2:
            return [0 for i in range(len(nums))]

        

        
        hashMap = {}

        fullProduct = 1
        product = 1

        result = []

        for n in nums:
            fullProduct *= n
            if n != 0:
                product *= n
                hashMap[n] = n
        
        for n in nums:
            if n == 0:
                result.append(int(product))
            else:
                result.append(int(fullProduct/n))
        
        return result

