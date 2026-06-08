class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def getTime(car):
            return (target - car[0]) / car[1]

        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        fleet = []

        for car in cars:
            time_to_target = getTime(car)

            if not fleet or fleet[-1] < time_to_target:
                fleet.append(time_to_target)
        
        return len(fleet)
