# Assessment 3.2 - Queue (FIFO, dynamic)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Queue (front -> rear):", self.items)


def main():
    text = input("Enter letters separated by spaces (press Enter for F L O R E S): ").strip()
    letters = text.upper().split() if text else list("FLORES")

    queue = Queue()
    for letter in letters:                     # enqueue one by one
        queue.enqueue(letter)
        print(f"Enqueued: {letter}")

    print()
    queue.display()

    print("\nDequeuing letters from the front...")
    while not queue.is_empty():
        removed = queue.dequeue()
        print(f"Dequeued: {removed}  ->  ", end="")
        queue.display()

    print("\nThe queue is now empty.")


if __name__ == "__main__":
    main()