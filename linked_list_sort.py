"""
Linked List Sorting Program

This module implements a singly linked list with various sorting algorithms:
- Merge Sort (O(n log n) - most efficient for linked lists)
- Bubble Sort (O(n²) - for comparison)
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
        """Append a value to the end of the list."""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, val):
        """Prepend a value to the beginning of the list."""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def from_list(self, values):
        """Build the linked list from a Python list."""
        self.head = None
        for val in values:
            self.append(val)

    def __str__(self):
        """Return a string representation of the linked list."""
        values = self.to_list()
        return " -> ".join(map(str, values)) + " -> None"

    def __len__(self):
        """Return the length of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # ==================== Sorting Algorithms ====================

    def merge_sort(self):
        """
        Sort the linked list using merge sort algorithm.
        Time Complexity: O(n log n)
        Space Complexity: O(log n) for recursion stack
        """
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        """Recursive merge sort implementation."""
        if not head or not head.next:
            return head

        # Split the list into two halves
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

    def bubble_sort(self):
        """
        Sort the linked list using bubble sort algorithm.
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current.next:
                if current.val > current.next.val:
                    # Swap values
                    current.val, current.next.val = current.next.val, current.val
                    swapped = True
                current = current.next

    def insertion_sort(self):
        """
        Sort the linked list using insertion sort algorithm.
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        if not self.head or not self.head.next:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def _sorted_insert(self, sorted_head, new_node):
        """Insert a node into a sorted linked list."""
        if not sorted_head or sorted_head.val >= new_node.val:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.val < new_node.val:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_head


def demo():
    """Demonstrate the linked list sorting functionality."""
    print("=" * 50)
    print("Linked List Sorting Demo")
    print("=" * 50)

    # Test data
    test_values = [64, 34, 25, 12, 22, 11, 90, 5]

    # Merge Sort Demo
    print("\n1. Merge Sort (Most Efficient - O(n log n))")
    print("-" * 40)
    ll1 = LinkedList()
    ll1.from_list(test_values)
    print(f"Original: {ll1}")
    ll1.merge_sort()
    print(f"Sorted:   {ll1}")

    # Bubble Sort Demo
    print("\n2. Bubble Sort (O(n²))")
    print("-" * 40)
    ll2 = LinkedList()
    ll2.from_list(test_values)
    print(f"Original: {ll2}")
    ll2.bubble_sort()
    print(f"Sorted:   {ll2}")

    # Insertion Sort Demo
    print("\n3. Insertion Sort (O(n²))")
    print("-" * 40)
    ll3 = LinkedList()
    ll3.from_list(test_values)
    print(f"Original: {ll3}")
    ll3.insertion_sort()
    print(f"Sorted:   {ll3}")

    # Edge cases
    print("\n4. Edge Cases")
    print("-" * 40)

    # Empty list
    empty_ll = LinkedList()
    empty_ll.merge_sort()
    print(f"Empty list sorted: {empty_ll}")

    # Single element
    single_ll = LinkedList()
    single_ll.append(42)
    single_ll.merge_sort()
    print(f"Single element sorted: {single_ll}")

    # Already sorted
    sorted_ll = LinkedList()
    sorted_ll.from_list([1, 2, 3, 4, 5])
    sorted_ll.merge_sort()
    print(f"Already sorted list: {sorted_ll}")

    # Reverse sorted
    reverse_ll = LinkedList()
    reverse_ll.from_list([5, 4, 3, 2, 1])
    reverse_ll.merge_sort()
    print(f"Reverse sorted list: {reverse_ll}")

    print("\n" + "=" * 50)
    print("Demo Complete!")
    print("=" * 50)


if __name__ == "__main__":
    demo()
