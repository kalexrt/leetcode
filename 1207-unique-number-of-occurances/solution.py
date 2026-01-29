class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq:dict ={}

        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        count = set(freq.values())

        if len(count) != len(freq):
            return False

        return True
