"""
Linked List Sort Program

This module implements a singly linked list with a merge sort algorithm
to sort the list in ascending order. Merge sort is optimal for linked lists
as it doesn't require random access and runs in O(n log n) time complexity.
"""


class ListNode:
    """A node in a singly linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """A singly linked list with sorting capability."""

    def __init__(self):
        self.head = None

    def append(self, val):
        """Add a new node with the given value to the end of the list."""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        """Convert the linked list to a Python list for easy viewing."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def from_list(self, values):
        """Create a linked list from a Python list."""
        self.head = None
        for val in values:
            self.append(val)

    def sort(self):
        """Sort the linked list in ascending order using merge sort."""
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        """Recursively sort the linked list using merge sort algorithm."""
        # Base case: empty list or single node
        if not head or not head.next:
            return head

        # Split the list into two halves
        mid = self._get_middle(head)
        mid_next = mid.next
        mid.next = None

        # Recursively sort both halves
        left = self._merge_sort(head)
        right = self._merge_sort(mid_next)

        # Merge the sorted halves
        return self._merge(left, right)

    def _get_middle(self, head):
        """Find the middle node of the linked list using slow/fast pointers."""
        if not head:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, left, right):
        """Merge two sorted linked lists into one sorted list."""
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # Attach remaining nodes
        current.next = left if left else right

        return dummy.next


def main():
    """Demonstrate the linked list sort functionality."""
    print("Linked List Sort Demo")
    print("=" * 40)

    # Example 1: Sort a list of integers
    ll = LinkedList()
    values = [4, 2, 1, 3, 5]
    ll.from_list(values)
    print(f"\nOriginal list: {ll.to_list()}")
    ll.sort()
    print(f"Sorted list:   {ll.to_list()}")

    # Example 2: Sort a larger unsorted list
    ll2 = LinkedList()
    values2 = [64, 34, 25, 12, 22, 11, 90]
    ll2.from_list(values2)
    print(f"\nOriginal list: {ll2.to_list()}")
    ll2.sort()
    print(f"Sorted list:   {ll2.to_list()}")

    # Example 3: Already sorted list
    ll3 = LinkedList()
    values3 = [1, 2, 3, 4, 5]
    ll3.from_list(values3)
    print(f"\nOriginal list: {ll3.to_list()}")
    ll3.sort()
    print(f"Sorted list:   {ll3.to_list()}")

    # Example 4: Reverse sorted list
    ll4 = LinkedList()
    values4 = [5, 4, 3, 2, 1]
    ll4.from_list(values4)
    print(f"\nOriginal list: {ll4.to_list()}")
    ll4.sort()
    print(f"Sorted list:   {ll4.to_list()}")

    # Example 5: Single element
    ll5 = LinkedList()
    ll5.from_list([42])
    print(f"\nOriginal list: {ll5.to_list()}")
    ll5.sort()
    print(f"Sorted list:   {ll5.to_list()}")

    # Example 6: Empty list
    ll6 = LinkedList()
    print(f"\nOriginal list: {ll6.to_list()}")
    ll6.sort()
    print(f"Sorted list:   {ll6.to_list()}")

    print("\n" + "=" * 40)
    print("All examples completed successfully!")


if __name__ == "__main__":
    main()
