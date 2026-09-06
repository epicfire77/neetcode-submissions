class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(key = lambda x: x[0])
        cars = deque(cars)
        print(cars)
        count = 1
        prev = cars.pop()
        while cars:
            car = cars.pop()
            print(car, prev, self.willCatch(car, prev, target))
            if not self.willCatch(car, prev, target):
                count += 1
                prev = car
            
        return count
        
    def willCatch(self, car1, car2, target):
        if car1[1] < car2[1]:
            return False
        if car1[1] == car2[1]:
            return car1[0] == car2[0]
        timeLeft = (target - car2[0])/car2[1]
        timeNeeded = (car2[0] - car1[0])/(car1[1] - car2[1])
        return timeLeft >= timeNeeded