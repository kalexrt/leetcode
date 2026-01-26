class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        delete:bool = False
        zero_idx = deque()
        max:int = 0
        count:int = 0
        no_of_zero: int = 0
        l: int = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
            elif no_of_zero < 1:
                no_of_zero += 1
                zero_idx.append(r)
                delete = True
            else:
                l = zero_idx.popleft() 
                zero_idx.append(r)
                l += 1
                count = r-l

            if count > max:
                    max = count

        if not delete:
            max -= 1
        return max