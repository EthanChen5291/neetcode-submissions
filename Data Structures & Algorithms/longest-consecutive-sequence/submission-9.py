class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # O(n) to build
        max_len = 0

        for n in num_set:
            # Check if 'n' is the start of a sequence
            if (n - 1) not in num_set:
                curr_num = n
                curr_len = 1

                # Keep looking for the next numbers in the streak
                while (curr_num + 1) in num_set:
                    curr_num += 1
                    curr_len += 1
                
                max_len = max(max_len, curr_len)
        
        return max_len