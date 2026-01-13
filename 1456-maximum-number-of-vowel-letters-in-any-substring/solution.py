class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel:set = {'a','e','i','o','u'}
        max:int = 0
        count:int = 0
        for i in range(len(s)):

            if i >= k:
                if s[i-k] in vowel:
                    count -= 1

            if s[i] in vowel:
                count += 1           
                if count > max:
                    max = count

                    if max == k:
                        return k

        return max