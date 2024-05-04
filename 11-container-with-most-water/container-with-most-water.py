class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxa = l = 0
        leng = r = len(height) - 1
        while l != r:
            area = min(height[l],height[r]) * leng

            if area > maxa:
                maxa = area
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            leng -= 1
        return maxa
            

            




        