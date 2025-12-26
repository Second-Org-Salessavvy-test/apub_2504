"""
Linked List Sort Implementation

This module provides a singly linked list implementation with merge sort
for efficient O(n log n) sorting.
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
        """Append a value to the end of the list."""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def to_list(self):
        """Convert linked list to Python list for easy viewing."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def from_list(self, values):
        """Build linked list from a Python list."""
        self.head = None
        for val in values:
            self.append(val)

    def sort(self):
        """Sort the linked list using merge sort."""
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        """Recursively sort the linked list using merge sort."""
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
        """Find the middle node using slow/fast pointer technique."""
        if not head:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, left, right):
        """Merge two sorted linked lists."""
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


def sort_linked_list(values):
    """
    Convenience function to sort a list of values using linked list merge sort.

    Args:
        values: A list of comparable values to sort

    Returns:
        A sorted list of values
    """
    ll = LinkedList()
    ll.from_list(values)
    ll.sort()
    return ll.to_list()


if __name__ == "__main__":
    # Example usage
    print("Linked List Sort Demo")
    print("=" * 40)

    # Test case 1: Random integers
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal: {test_data}")
    sorted_data = sort_linked_list(test_data)
    print(f"Sorted:   {sorted_data}")

    # Test case 2: Already sorted
    test_data = [1, 2, 3, 4, 5]
    print(f"\nOriginal: {test_data}")
    sorted_data = sort_linked_list(test_data)
    print(f"Sorted:   {sorted_data}")

    # Test case 3: Reverse sorted
    test_data = [5, 4, 3, 2, 1]
    print(f"\nOriginal: {test_data}")
    sorted_data = sort_linked_list(test_data)
    print(f"Sorted:   {sorted_data}")

    # Test case 4: Empty list
    test_data = []
    print(f"\nOriginal: {test_data}")
    sorted_data = sort_linked_list(test_data)
    print(f"Sorted:   {sorted_data}")

    # Test case 5: Single element
    test_data = [42]
    print(f"\nOriginal: {test_data}")
    sorted_data = sort_linked_list(test_data)
    print(f"Sorted:   {sorted_data}")

    # Test case 6: Duplicates
    test_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"\nOriginal: {test_data}")
    sorted_data = sort_linked_list(test_data)
    print(f"Sorted:   {sorted_data}")

    print("\n" + "=" * 40)
    print("All tests completed!")
