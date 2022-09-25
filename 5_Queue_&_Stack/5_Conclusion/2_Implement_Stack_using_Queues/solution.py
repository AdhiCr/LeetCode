class MyStack:

    def __init__(self):
        self.queue_1 = []

    def push(self, x: int) -> None:
        self.queue_1.append(x)

    def pop(self) -> int:
        for _ in range(len(self.queue_1) - 1):
            self.push(self.queue_1.pop(0))
        return self.queue_1.pop(0)

    def top(self) -> int:
        return self.queue_1[-1]

    def empty(self) -> bool:
        return not self.queue_1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
dummy = MyStack()
dummy.push(1)
dummy.push(2)
print(dummy.top())
print(dummy.pop())
print(dummy.empty())