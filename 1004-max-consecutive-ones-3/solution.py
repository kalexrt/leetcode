from collections import deque

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_idx = deque()
        max:int = 0
        count:int = 0
        no_of_zero: int = 0
        l: int = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
            elif no_of_zero < k:
                no_of_zero += 1
                count += 1
                zero_idx.append(r)
            else:
                if k != 0:
                    l = zero_idx.popleft() 
                    zero_idx.append(r)
                    count = r - l
                    l += 1

                else:    
                    l = r
                    count = 0  

            if count > max:
                    max = count

        return max