class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        pairs:int = 0
        occurances = {}
        for i in grid:
            temp = ','.join(map(str, i))
            
            if temp in occurances:
                occurances[temp] += 1
            else:
                occurances[temp] = 1
        
        for j in range(len(grid)):
            elem = str(grid[0][j])
            for i in range(1,len(grid)):
                elem += "," + str(grid[i][j])
            if elem in occurances:
                pairs += occurances[elem]
        return pairs
            