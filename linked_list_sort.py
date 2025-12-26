#!/usr/bin/env python3
"""
Linked List Sorting Program

This module provides a singly linked list implementation with various sorting algorithms.
The primary sorting algorithm is Merge Sort, which is optimal for linked lists with O(n log n)
time complexity and O(1) space complexity (for the iterative version).
"""


class ListNode:
    """A node in a singly linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


class LinkedList:
    """A singly linked list with sorting capabilities."""

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

    def prepend(self, val):
        """Add a new node with the given value to the beginning of the list."""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def from_list(self, values):
        """Create a linked list from a Python list of values."""
        for val in values:
            self.append(val)
        return self

    def to_list(self):
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def __str__(self):
        """Return a string representation of the linked list."""
        values = self.to_list()
        return " -> ".join(map(str, values)) if values else "Empty List"

    def __len__(self):
        """Return the length of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def sort(self, algorithm="merge"):
        """
        Sort the linked list in ascending order.

        Args:
            algorithm: The sorting algorithm to use. Options:
                - "merge": Merge Sort (default, O(n log n) time, O(log n) space)
                - "insertion": Insertion Sort (O(n^2) time, O(1) space)
        """
        if algorithm == "merge":
            self.head = self._merge_sort(self.head)
        elif algorithm == "insertion":
            self.head = self._insertion_sort(self.head)
        else:
            raise ValueError(f"Unknown sorting algorithm: {algorithm}")

    def _merge_sort(self, head):
        """
        Sort the linked list using Merge Sort algorithm.

        Time Complexity: O(n log n)
        Space Complexity: O(log n) due to recursion stack
        """
        if not head or not head.next:
            return head

        # Find the middle of the list
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        # Recursively sort both halves
        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        # Merge the sorted halves
        return self._merge(left, right)

    def _get_middle(self, head):
        """Find the middle node of the linked list using slow/fast pointer technique."""
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

    def _insertion_sort(self, head):
        """
        Sort the linked list using Insertion Sort algorithm.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        current = head

        while current:
            next_node = current.next

            # Find the correct position to insert
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current node
            current.next = prev.next
            prev.next = current

            current = next_node

        return dummy.next


def sort_linked_list(head):
    """
    Standalone function to sort a linked list using Merge Sort.

    Args:
        head: The head node of the linked list

    Returns:
        The head node of the sorted linked list
    """
    if not head or not head.next:
        return head

    # Find middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    # Sort both halves
    left = sort_linked_list(head)
    right = sort_linked_list(mid)

    # Merge sorted halves
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

    current.next = left or right

    return dummy.next


def demo():
    """Demonstrate the linked list sorting functionality."""
    print("=" * 50)
    print("Linked List Sorting Demo")
    print("=" * 50)

    # Example 1: Using LinkedList class with merge sort
    print("\n1. Merge Sort (default):")
    ll = LinkedList()
    ll.from_list([4, 2, 1, 3, 5, 7, 6])
    print(f"   Original: {ll}")
    ll.sort()
    print(f"   Sorted:   {ll}")

    # Example 2: Using LinkedList class with insertion sort
    print("\n2. Insertion Sort:")
    ll2 = LinkedList()
    ll2.from_list([64, 34, 25, 12, 22, 11, 90])
    print(f"   Original: {ll2}")
    ll2.sort(algorithm="insertion")
    print(f"   Sorted:   {ll2}")

    # Example 3: Using standalone function
    print("\n3. Standalone sort function:")
    head = ListNode(3)
    head.next = ListNode(1)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(5)

    original = []
    curr = head
    while curr:
        original.append(curr.val)
        curr = curr.next
    print(f"   Original: {' -> '.join(map(str, original))}")

    sorted_head = sort_linked_list(head)

    sorted_vals = []
    curr = sorted_head
    while curr:
        sorted_vals.append(curr.val)
        curr = curr.next
    print(f"   Sorted:   {' -> '.join(map(str, sorted_vals))}")

    # Example 4: Edge cases
    print("\n4. Edge Cases:")

    # Empty list
    empty = LinkedList()
    empty.sort()
    print(f"   Empty list: {empty}")

    # Single element
    single = LinkedList()
    single.from_list([42])
    single.sort()
    print(f"   Single element: {single}")

    # Already sorted
    sorted_list = LinkedList()
    sorted_list.from_list([1, 2, 3, 4, 5])
    sorted_list.sort()
    print(f"   Already sorted: {sorted_list}")

    # Reverse sorted
    reverse = LinkedList()
    reverse.from_list([5, 4, 3, 2, 1])
    reverse.sort()
    print(f"   Reverse sorted: {reverse}")

    # Duplicates
    duplicates = LinkedList()
    duplicates.from_list([3, 1, 2, 1, 3, 2])
    duplicates.sort()
    print(f"   With duplicates: {duplicates}")

    print("\n" + "=" * 50)
    print("Demo completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    demo()
