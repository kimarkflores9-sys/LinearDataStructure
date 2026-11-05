# Assessment 3.2 - Stack (LIFO, dynamic)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack (bottom -> top):", self.items)


def main():
    text = input("Enter letters separated by spaces (press Enter for F L O R E S): ").strip()
    letters = text.upper().split() if text else list("FLORES")

    stack = Stack()
    for letter in letters:                     # push one by one
        stack.push(letter)
        print(f"Pushed: {letter}")

    print()
    stack.display()

    print("\nPopping letters from the top...")
    while not stack.is_empty():
        popped = stack.pop()
        print(f"Popped: {popped}  ->  ", end="")
        stack.display()

    print("\nThe stack is now empty.")


if __name__ == "__main__":
    main()