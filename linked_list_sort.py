"""
Linked List Sorting Program

This module implements a singly linked list with various sorting algorithms:
- Merge Sort (O(n log n) time, O(log n) space for recursion)
- Insertion Sort (O(n^2) time, O(1) space)
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
        """Add a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node with the given data to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        """Convert the linked list to a Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, items):
        """Build the linked list from a Python list."""
        self.head = None
        for item in items:
            self.append(item)

    def __str__(self):
        """Return a string representation of the linked list."""
        if not self.head:
            return "[]"
        values = self.to_list()
        return " -> ".join(str(v) for v in values)

    def __len__(self):
        """Return the length of the linked list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # ==================== Merge Sort ====================

    def merge_sort(self):
        """Sort the linked list using merge sort algorithm."""
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        """Recursively sort the linked list using merge sort."""
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

    # ==================== Insertion Sort ====================

    def insertion_sort(self):
        """Sort the linked list using insertion sort algorithm."""
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
        """Insert a node into its correct position in a sorted list."""
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
    """Demonstrate the linked list sorting functionality."""
    print("=" * 50)
    print("Linked List Sorting Demo")
    print("=" * 50)

    # Demo with integers
    print("\n--- Integer Sorting (Merge Sort) ---")
    ll = LinkedList()
    test_data = [64, 34, 25, 12, 22, 11, 90]
    ll.from_list(test_data)
    print(f"Original: {ll}")
    ll.merge_sort()
    print(f"Sorted:   {ll}")

    # Demo with insertion sort
    print("\n--- Integer Sorting (Insertion Sort) ---")
    ll2 = LinkedList()
    test_data2 = [5, 2, 8, 1, 9, 3]
    ll2.from_list(test_data2)
    print(f"Original: {ll2}")
    ll2.insertion_sort()
    print(f"Sorted:   {ll2}")

    # Demo with strings
    print("\n--- String Sorting (Merge Sort) ---")
    ll3 = LinkedList()
    string_data = ["banana", "apple", "cherry", "date", "apricot"]
    ll3.from_list(string_data)
    print(f"Original: {ll3}")
    ll3.merge_sort()
    print(f"Sorted:   {ll3}")

    # Demo with negative numbers
    print("\n--- Negative Numbers (Merge Sort) ---")
    ll4 = LinkedList()
    negative_data = [-5, 3, -1, 7, -8, 2, 0]
    ll4.from_list(negative_data)
    print(f"Original: {ll4}")
    ll4.merge_sort()
    print(f"Sorted:   {ll4}")

    print("\n" + "=" * 50)
    print("Demo Complete!")
    print("=" * 50)


if __name__ == "__main__":
    demo()
