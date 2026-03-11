def determine_shape(word: str, dictionary: dict[str: str]) -> str:
    """
    Determine the shape category of an item using the provided dictionary.

    Args:
        word: Item to find shape category for
        dictionary: Dictionary mapping shape names to lists of items

    Returns:
        Shape name if found, otherwise "No information about shape"
    """
    for shape, things in dictionary.items():
        if word in things:
            return shape
    return "No information about shape"


if __name__ == "__main__":
    dictionary = {}
    n = int(input("Enter the count of elements: "))
    for _ in range(n):
        shape, *things = input().split()
        dictionary[shape] = things
    determined_word = input("Enter item to determine shape: ")
    print(determine_shape(determined_word, dictionary))
