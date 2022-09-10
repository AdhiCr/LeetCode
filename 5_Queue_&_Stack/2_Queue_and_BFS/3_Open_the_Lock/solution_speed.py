from typing import List
from collections import deque


class Solution:
    def rotateRings(self, current_state: str) -> List[str]:
        rotate_possibility = {
            '0': ['9', '1'],
            '1': ['0', '2'],
            '2': ['1', '3'],
            '3': ['2', '4'],
            '4': ['3', '5'],
            '5': ['4', '6'],
            '6': ['5', '7'],
            '7': ['6', '8'],
            '8': ['7', '9'],
            '9': ['8', '0'],
        }
        new_states = []
        for i in range(4):
            new_states.extend([
                current_state[:i] + rotate_possibility[current_state[i]][0] + current_state[i+1:],
                current_state[:i] + rotate_possibility[current_state[i]][1] + current_state[i+1:]
            ])
        return new_states

    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        from_start = set(["0000"])
        from_target = set([target])
        rots = 0
        visited = set(deadends)

        while from_start and from_target:
            if len(from_start) > len(from_target):
                from_start, from_target = from_target, from_start

            new_positions = set()

            for current_state in from_start:
                for new_position in self.rotateRings(current_state):
                    if new_position in from_target:
                        return rots + 1
                    if new_position not in visited:
                        new_positions.add(new_position)
                        visited.add(new_position)
            from_start = new_positions
            rots += 1
        return -1


dummy = Solution()
print(dummy.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
print(dummy.openLock(deadends = ["8888"], target = "0009"))
print(dummy.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))