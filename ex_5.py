def count_descendants(
        person: str, tree: dict[str: list[str]]
) -> int:
    """
        Count the total number of descendants for a given person in a family tree.

        Args:
            person: Name of the person to count descendants for
            tree: Dictionary mapping parent names to lists of their children

        Returns:
            Total number of descendants
        """
    if person not in tree:
        return 0
    total = len(tree[person])
    for child in tree[person]:
        total += count_descendants(child, tree)
    return total


if __name__ == "__main__":
    n = int(input("Enter the count of branches: "))
    tree = {}
    for _ in range(n):
        parent, child = input().split()
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)
    person = input("Enter name to count descendants: ")
    print(count_descendants(person, tree))
