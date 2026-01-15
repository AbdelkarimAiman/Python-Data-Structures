class Node:
    """
    Node class represents a single element in the linked list.
    --------------------------------------------
    Attributes:
    - value: the data stored in the node
    - next: reference to the next node (None if last)
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    """
    LinkedList class manages the linked list.
    -----------------------------------------
    Attributes:
    - head: the first node in the list
    - tail: the last node for efficient append
    - count: total number of nodes in the list
    """

    def __init__(self):
        self.head = None  # points to the first node
        self.tail = None  # points to the last node
        self.count = 0    # number of nodes

    # -----------------------------
    # 1. Append a value to the end
    # -----------------------------
    def append(self, value):
        """
        Add a new node at the end of the list.
        This is now O(1) with tail reference.
        """
        new_node = Node(value)

        if self.head is None:
            # List is empty, new node becomes head and tail
            self.head = self.tail = new_node
        else:
            # attach to the end and update tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1  # increment size

    # -----------------------------
    # 2. Print the linked list
    # -----------------------------
    def print_list(self):
        """
        Print all values in the list visually:
        Example: 10 -> 20 -> 30 -> None
        """
        pointer = self.head
        while pointer:
            print(pointer.value, end=" -> ")
            pointer = pointer.next
        print("None")

    # -----------------------------
    # 3. Get value by index
    # -----------------------------
    def get(self, index):
        """
        Get the value at a specific index.
        Raises IndexError if index is invalid.
        """
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")

        pointer = self.head
        for _ in range(index):
            pointer = pointer.next
        return pointer.value

    # -----------------------------
    # 4. Find index of a value
    # -----------------------------
    def index_of(self, value):
        """
        Return the first index of the value.
        If not found, return -1.
        """
        pointer = self.head
        idx = 0
        while pointer:
            if pointer.value == value:
                return idx
            pointer = pointer.next
            idx += 1
        return -1

    # -----------------------------
    # 5. Check if value exists
    # -----------------------------
    def contains(self, value):
        """
        Returns True if value exists, else False.
        """
        return self.index_of(value) != -1

    # -----------------------------
    # 6. Return size of list
    # -----------------------------
    def size(self):
        return self.count

    # -----------------------------
    # 7. Add value at the beginning
    # -----------------------------
    def add_first(self, value):
        """
        Add a new node at the start.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            # if list was empty, tail also points to new node
            self.tail = new_node

        self.count += 1

    # -----------------------------
    # 8. Remove first node
    # -----------------------------
    def remove_first(self):
        """
        Remove the first node of the list.
        """
        if self.head is None:
            raise Exception("List is empty")

        self.head = self.head.next
        self.count -= 1

        if self.head is None:
            # list became empty, tail should also be None
            self.tail = None

    # -----------------------------
    # 9. Remove last node
    # -----------------------------
    def remove_last(self):
        """
        Remove the last node in the list.
        """
        if self.head is None:
            raise Exception("List is empty")

        if self.head == self.tail:
            # only one node
            self.head = self.tail = None
            self.count = 0
            return

        pointer = self.head
        while pointer.next != self.tail:
            pointer = pointer.next

        pointer.next = None
        self.tail = pointer
        self.count -= 1

    # -----------------------------
    # 10. Remove node by value
    # -----------------------------
    def remove_value(self, value):
        """
        Remove first node containing the value.
        """
        if self.head is None:
            raise Exception("List is empty")

        if self.head.value == value:
            return self.remove_first()

        pointer = self.head
        while pointer.next and pointer.next.value != value:
            pointer = pointer.next

        if pointer.next is None:
            print("Value not found")
            return

        if pointer.next == self.tail:
            self.tail = pointer

        pointer.next = pointer.next.next
        self.count -= 1


