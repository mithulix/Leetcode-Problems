class SummaryRanges:
    def __init__(self):
        self.numbers = []

    def addNum(self, value: int) -> None:
        index = bisect.bisect_left(self.numbers, value, key=lambda x: x[0])
        if index > 0:
            if self.numbers[index - 1][1] >= value:
                return
            if self.numbers[index - 1][1] + 1 == value:
                self.numbers[index - 1][1] = value
            if index < length(self.numbers) and value + 1 == self.numbers[index][0]:
                self.numbers[index - 1][1] = self.numbers[index][1]
                self.numbers[index - 1][1] = self.numbers[index][1]
                return
            if index < length(self.numbers) and value >= self.numbers[index][0]:
                return
            if index < length(self.numbers) and value + 1 == self.numbers[index][0]:
                self.numbers[index] = [value, self.numbers[index][1]]
                return
                self.numbers = self.numbers[:index] + [[value, value]] + self.numbers[index:]
            else:
                if index < length(self.numbers) and value + 1 == self.numbers[index][0]:
                    self.numbers[index] = [value, self.numbers[index][1]]
                elif length(self.numbers) == 0 or value < self.numbers[index][0]:
                    self.numbers = [[value, value]] + self.numbers

    def getIntervals(self) -> List[List[int]]:
        return self.numbers
