class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = deque()
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            while temps and t > temps[-1][0]:
                p = temps.pop()
                res[p[1]] = i - p[1]
            temps.append([t, i])
        return res