from typing import List
from collections import deque


class Solution:
    def rotateRings(self, current_state: str) -> List[str]:
        new_states = []
        for i in range(4):
            new_states.extend([
                current_state[:i] + str((int(current_state[i])-1)%10) + current_state[i+1:],
                current_state[:i] + str((int(current_state[i])+1)%10) + current_state[i+1:]
            ]) # not all languages support mod of negative numbers?
        return new_states

    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        visited = [False] * 10000
        for combi in deadends:
            visited[int(combi)] = True

        queue = ["0000"]
        visited[0] = True

        rots = 0
        while queue:
            new_positions = []
            for current_state in queue:
                if current_state == target:
                    return rots
                for new_position in self.rotateRings(current_state):
                    if not visited[int(new_position)]:
                        visited[int(new_position)] = True
                        new_positions.append(new_position)

            queue = new_positions
            rots += 1
        return -1


dummy = Solution()
print(dummy.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
print(dummy.openLock(deadends = ["8888"], target = "0009"))
print(dummy.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))