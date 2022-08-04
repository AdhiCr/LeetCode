from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while (curr and curr.next):
            # if curr.prev:
            #     print(f"Prev_Value: {curr.prev.val}")
            # else:
            #     print(None)
            # print(f"Current_value: {curr.val}")
            # if curr.next:
            #     print(f"Next_value: {curr.next.val}")
            # else:
            #     print(None)
            # print("\n")
            if curr.child:
                last_of_child = self.flatten_child(curr.child)

                last_of_child.next = curr.next
                curr.child.prev = curr

                curr.next = curr.child
                curr.child = None

                # print(f"CHILD OF {curr.val} AFTER MERGE: {curr.child}")
                # print(f"NEXT OF {curr.val} AFTER MERGE: {curr.next.val}")

                curr = last_of_child.next
                curr.prev = last_of_child
                # print(f"PREVIOUS OF {curr.val} AFTER MERGE: {curr.prev.val}")

            else:

                # print(f"Current_child_value: {curr.child}")
                curr = curr.next

            #         curr = head
        #         while(curr and curr.next):
        #             # print(f"Current_value: {curr.val}")
        #             # print(f"Child_Node: {curr.child}")

        #             if curr.prev:
        #                 print(f"Prev_Value: {curr.prev.val}")
        #             else:
        #                 print(None)
        #             print(f"Current_value: {curr.val}")
        #             if curr.next:
        #                 print(f"Next_value: {curr.next.val}")
        #             else:
        #                 print(None)
        #             print("\n")

        #             curr = curr.next

        #         if curr.prev:
        #             print(f"Prev_Value: {curr.prev.val}")
        #         else:
        #             print(None)
        #         print(f"Current_value: {curr.val}")
        #         if curr.next:
        #             print(f"Next_value: {curr.next.val}")
        #         else:
        #             print(None)
        #         print("\n")
        #         # print(f"Current_value: {curr.val}")
        #         # print(f"Child_Node: {curr.child}")
        #         curr = curr.prev
        #         while(curr and curr.prev):

        #             if curr.prev:
        #                 print(f"Prev_Value: {curr.prev.val}")
        #             else:
        #                 print(None)
        #             print(f"Current_value: {curr.val}")
        #             if curr.next:
        #                 print(f"Next_value: {curr.next.val}")
        #             else:
        #                 print(None)
        #             print("\n")
        #             # print(f"Current_value: {curr.val}")
        #             # print(f"Child_Node: {curr.child}")
        #             curr = curr.prev
        #         print("Finished_backwards_pass")
        #         curr = curr.prev

        return head

    def flatten_child(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        # print(f"entering recursive method with value: {head.val}")

        while (curr and curr.next):
            # if curr.prev:
            #     print(f"Prev_Value: {curr.prev.val}")
            # else:
            #     print(None)
            # print(f"Current_value: {curr.val}")
            # if curr.next:
            #     print(f"Next_value: {curr.next.val}")
            # else:
            #     print(None)
            # print("\n")
            if curr.child:
                last_of_child = self.flatten_child(curr.child)

                last_of_child.next = curr.next
                curr.child.prev = curr

                curr.next = curr.child
                curr.child = None

                # print(f"CHILD OF {curr.val} AFTER MERGE: {curr.child}")
                # print(f"NEXT OF {curr.val} AFTER MERGE: {curr.next.val}")

                curr = last_of_child.next
                curr.prev = last_of_child
                # print(f"PREVIOUS OF {curr.val} AFTER MERGE: {curr.prev.val}")
            else:

                # print(f"Current_child_value: {curr.child}")
                curr = curr.next

        # print(f"Current_value: {curr.val}")

        # print(f"Current_child_value: {curr.child}")
        # print(f"exiting recursive method with value: {curr.val}")
        return curr
