def create_dict(words: list[str]) -> dict[str: int]:
    """
       Create a dictionary counting occurrences of each word.

       Args:
           words: List of words to count

       Returns:
           Dictionary with words as keys and their frequencies as values
       """
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict


def print_sorted_words(words_dict: dict[str: int]) -> None:
    """
       Print words sorted by frequency in descending order.

       Args:
           words_dict: Dictionary with word-frequency pairs
           
        Returns:
            None
       """
    sorted_words = sorted(
        words_dict, key=lambda x: words_dict[x], reverse=True
    )
    for word in sorted_words:
        print(word)


if __name__ == '__main__':
    words = input('Enter the words: ').split()
    words_dict = create_dict(words)
    print_sorted_words(words_dict)
