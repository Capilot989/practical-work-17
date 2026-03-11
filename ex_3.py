def determine_antonym(word: str, dictionary: dict[str: str]) -> str:
    """
        Find the antonym of a word using the provided dictionary.

        Args:
            word: Word to find antonym for
            dictionary: Dictionary mapping words to their antonyms

        Returns:
            Antonym if found in dictionary, otherwise the original word
        """
    if word in dictionary:
        return dictionary[word]
    return word


if __name__ == "__main__":
    dictionary = {}
    n = int(input("Enter the count of antonyms: "))
    for _ in range(n):
        word, antonym = map(str, input().split())
        dictionary[word] = antonym
    determined_word = input('Enter the word to find antonym: ')

    print(determine_antonym(determined_word, dictionary))
