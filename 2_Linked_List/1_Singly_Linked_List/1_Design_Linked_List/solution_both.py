class MyLinkedList:
    def __init__(self):
        self.data = []

    def get(self, index: int) -> int:
        if 0 <= index < len(self.data):
            return self.data[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.data.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.data.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self.data):
            self.data.insert(index, val)
        # elif index == len(self.data):
        #     self.data.append(val)
        else:
            pass

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.data):
            self.data.pop(index)
