"""2. Find the Middle Element of a Linked List

Problem Statement
Find the middle node of a given singly linked list in a single traversal. If there are two middle nodes (even length), return the second middle node.
10 -> 20 -> 30 -> 40 -> 50 -> 60 40 
----------------------------------------------------------------"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1

slow=head
fast=head

while fast and fast.next:
    slow=slow.next
    fast=fast.next.next
print("MIddle element is", slow.data)    


"""4. Detect a Cycle/Loop in a Linked List [1]
Problem Statement
Determine if a linked list contains a loop (cycle). If a loop exists, return True, otherwise return False
--------------------------------------------------------------------------------"""
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


"""21. Merge Two Sorted Lists


You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return .
 
Example 1:Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:Input: list1 = [], list2 = []
Output: []

Example 3:Input: list1 = [], list2 = [0]
Output: [0]

 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order
---------------------------------------------------"""
dummy=ListNode(0)
tail=dummy
while list1 and list2:
    if list1.val<list2.val:
        tail.next=list1
        list1=list1.next
    else:
        tail.next=list2
        list2=list2.next
    tail=tail.next   
if list1:
    tail.next=list1
elif list2:
    tail.next=list2