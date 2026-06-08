class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        times = []

        for car in cars:
            time = (target - car[0]) / car[1]
            times.append(time)
            if len(times) >= 2 and times[-2] >= times[-1]:
                times.pop()

        return len(times)
