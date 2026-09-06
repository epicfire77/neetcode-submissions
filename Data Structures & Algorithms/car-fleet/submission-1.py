class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # no increases in position
        # no decreases in time
        cars = sorted([[position[i], self.tarTime(position[i], speed[i], target)] for i in range(len(position))], key = lambda x: x[0])
        c = deque()
        print(cars)
        for car in cars:
            t = car[1]
            while c and t >= c[-1][1]:
                c.pop()
            c.append(car)
        return len(c)
        
    def tarTime(self, position, speed, target):
        return (target - position)/speed
        # if car1[1] < car2[1]:
        #     return False
        # if car1[1] == car2[1]:
        #     return car1[0] == car2[0]
        # timeLeft = (target - car2[0])/car2[1]
        # timeNeeded = (car2[0] - car1[0])/(car1[1] - car2[1])
        # return timeLeft >= timeNeeded