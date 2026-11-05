# Assessment 3.2 - Singly Linked List (dynamic)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_first(self):
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next
        return removed

    def is_empty(self):
        return self.head is None

    def display(self):
        current = self.head
        parts = []
        while current:
            parts.append(str(current.data))
            current = current.next
        parts.append("NULL")
        print(" -> ".join(parts))


def main():
    text = input("Enter letters separated by spaces (press Enter for F L O R E S): ").strip()
    letters = text.upper().split() if text else list("FLORES")

    linked_list = LinkedList()
    for letter in letters:                     # create the nodes
        linked_list.append(letter)

    print("\nLinked list:")
    linked_list.display()

    print("\nDeleting the first node one at a time...")
    while not linked_list.is_empty():
        removed = linked_list.delete_first()
        print(f"Deleted: {removed}  ->  ", end="")
        linked_list.display()

    print("\nThe linked list is now empty.")


if __name__ == "__main__":
    main()