from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        available_keys = [0]
        while available_keys:
            room_no = available_keys.pop(0)
            if rooms[room_no]:
                for room_key in rooms[room_no]:
                    available_keys.append(room_key)
                rooms[room_no] = []

        return not any(rooms)


dummy = Solution()
print(dummy.canVisitAllRooms(rooms = [[1],[2],[3],[]]))
print(dummy.canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]))