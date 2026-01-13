class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def insert_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def insert_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1

    def delete_first(self):
        if self.head is None:
            raise IndexError("List is empty")

        self.head = self.head.next
        self.size -= 1

    def delete_last(self):
        if self.head is None:
            raise IndexError("List is empty")

        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next and current.next.next:
                current = current.next
            current.next = None

        self.size -= 1
