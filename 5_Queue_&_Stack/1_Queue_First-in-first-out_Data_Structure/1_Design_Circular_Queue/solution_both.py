class MyCircularQueue:

    def __init__(self, k: int):
        self.max_len = k
        self.queue_list = [0] * self.max_len
        self.start_pointer = 0
        self.filled_qty = 0

    def enQueue(self, value: int) -> bool:
        if self.filled_qty == self.max_len:
            return False
        else:
            self.queue_list[(self.start_pointer + self.filled_qty)%self.max_len] = value
            self.filled_qty += 1
            return True

    def deQueue(self) -> bool:
        if self.filled_qty == 0:
            return False
        else:
            self.start_pointer = (self.start_pointer + 1) % self.max_len
            self.filled_qty -= 1
            return True

    def Front(self) -> int:
        if self.filled_qty == 0:
            return -1
        else:
            return self.queue_list[self.start_pointer]

    def Rear(self) -> int:
        if self.filled_qty == 0:
            return -1
        else:
            return self.queue_list[(self.start_pointer + self.filled_qty - 1) % self.max_len]

    def isEmpty(self) -> bool:
        return self.filled_qty == 0

    def isFull(self) -> bool:
        return self.filled_qty == self.max_len

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

dummy = MyCircularQueue(6)
print("null")
print(dummy.enQueue(6))
print(dummy.Rear())
print(dummy.Rear())
print(dummy.deQueue())
print(dummy.enQueue(5))
print(dummy.Rear())
print(dummy.deQueue())
print(dummy.Front())
print(dummy.deQueue())
print(dummy.deQueue())
print(dummy.deQueue())