class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        cpy = [[t, 0] for t in temperatures]
        for i in range(len(temperatures) - 2, -1, -1):
            j = 1
            while i + j < len(temperatures) and cpy[i + j][0] <= temperatures[i] and cpy[i + j][1] > 0:
                j += cpy[i + j][1]
            if cpy[i + j][0] <= temperatures[i]:
                j = 0
            cpy[i][1] = j
        
        return [k[1] for k in cpy]
