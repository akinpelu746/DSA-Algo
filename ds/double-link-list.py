class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_last(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.insert_first(data)
            return

        if index == self.size:
            self.insert_last(data)
            return

        new_node = Node(data)

        current = self.head
        for _ in range(index - 1):
            current = current.next

        new_node.prev = current.prev
        new_node.prev.next = new_node
        current.prev = new_node
        new_node.next = current

        self.size += 1

    def delete_first(self):
        if self.head is None:
            raise IndexError("List is empty")
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def delete_last(self):
        if self.tail is None:
            raise IndexError("List is empty")
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
