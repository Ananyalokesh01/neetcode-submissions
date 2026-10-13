
class MinStack:

    def __init__(self):
        self.values = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.values.append(val)

        if not self.min_values or val <= self.min_values[-1]:
            self.min_values.append(val)

    def pop(self) -> None:
        val = self.values.pop()

        if val == self.min_values[-1]:
            self.min_values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_values[-1]

