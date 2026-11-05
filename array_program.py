# Assessment 3.2 - Array (dynamic)

def get_letters():
    text = input("Enter letters separated by spaces (press Enter for F L O R E S): ").strip()
    return text.upper().split() if text else list("FLORES")


def main():
    array = get_letters()                      # create the array
    print("\nArray:", array)                    # display all letters

    print("\nRemoving letters one at a time...")
    while len(array) > 0:                      # remove until empty
        removed = array.pop(0)
        print(f"Removed: {removed}  ->  Array: {array}")

    print("\nThe array is now empty.")


if __name__ == "__main__":
    main()