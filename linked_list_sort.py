"""
Linked List Sorting Program

This module implements a singly linked list with multiple sorting algorithms:
- Merge Sort (O(n log n) - recommended for linked lists)
- Bubble Sort (O(n^2) - for educational purposes)
- Insertion Sort (O(n^2) - simple implementation)
"""


class Node:
    """A node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list with sorting capabilities."""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        """Convert linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, items):
        """Build linked list from a Python list."""
        self.head = None
        for item in items:
            self.append(item)

    def __str__(self):
        """Return string representation of the list."""
        if not self.head:
            return "Empty List"
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)

    def __len__(self):
        """Return the length of the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # ==================== Sorting Algorithms ====================

    def merge_sort(self):
        """
        Sort the linked list using Merge Sort algorithm.
        Time Complexity: O(n log n)
        Space Complexity: O(log n) for recursion stack

        This is the most efficient sorting algorithm for linked lists.
        """
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        """Recursive merge sort implementation."""
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
        dummy = Node(0)
        current = dummy

        while left and right:
            if left.data <= right.data:
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
        Sort the linked list using Bubble Sort algorithm.
        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Simple but inefficient for large lists.
        """
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current.next:
                if current.data > current.next.data:
                    # Swap data
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def insertion_sort(self):
        """
        Sort the linked list using Insertion Sort algorithm.
        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Good for small or nearly sorted lists.
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
        if not sorted_head or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_head


def demo():
    """Demonstrate the linked list sorting algorithms."""
    print("=" * 60)
    print("Linked List Sorting Program Demo")
    print("=" * 60)

    # Test data
    test_data = [64, 34, 25, 12, 22, 11, 90, 45, 33, 21]

    # Demo Merge Sort
    print("\n1. MERGE SORT (Recommended for Linked Lists)")
    print("-" * 40)
    ll1 = LinkedList()
    ll1.from_list(test_data)
    print(f"Original: {ll1}")
    ll1.merge_sort()
    print(f"Sorted:   {ll1}")

    # Demo Bubble Sort
    print("\n2. BUBBLE SORT")
    print("-" * 40)
    ll2 = LinkedList()
    ll2.from_list(test_data)
    print(f"Original: {ll2}")
    ll2.bubble_sort()
    print(f"Sorted:   {ll2}")

    # Demo Insertion Sort
    print("\n3. INSERTION SORT")
    print("-" * 40)
    ll3 = LinkedList()
    ll3.from_list(test_data)
    print(f"Original: {ll3}")
    ll3.insertion_sort()
    print(f"Sorted:   {ll3}")

    # Additional test cases
    print("\n" + "=" * 60)
    print("Additional Test Cases")
    print("=" * 60)

    # Empty list
    print("\nEmpty List:")
    empty_list = LinkedList()
    print(f"Before: {empty_list}")
    empty_list.merge_sort()
    print(f"After:  {empty_list}")

    # Single element
    print("\nSingle Element:")
    single = LinkedList()
    single.append(42)
    print(f"Before: {single}")
    single.merge_sort()
    print(f"After:  {single}")

    # Already sorted
    print("\nAlready Sorted:")
    sorted_list = LinkedList()
    sorted_list.from_list([1, 2, 3, 4, 5])
    print(f"Before: {sorted_list}")
    sorted_list.merge_sort()
    print(f"After:  {sorted_list}")

    # Reverse sorted
    print("\nReverse Sorted:")
    reverse_list = LinkedList()
    reverse_list.from_list([5, 4, 3, 2, 1])
    print(f"Before: {reverse_list}")
    reverse_list.merge_sort()
    print(f"After:  {reverse_list}")

    # Duplicates
    print("\nWith Duplicates:")
    dup_list = LinkedList()
    dup_list.from_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    print(f"Before: {dup_list}")
    dup_list.merge_sort()
    print(f"After:  {dup_list}")

    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    demo()
