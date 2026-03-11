def translate(phrase: str, dictionary: dict[str: str]) -> str:
    """
      Translate a phrase from Russian to English using the provided dictionary.

      Args:
          phrase: Russian phrase to translate
          dictionary: Dictionary mapping Russian words to English translations

      Returns:
          Translated phrase with words separated by spaces
      """
    result = ""
    for word in phrase.split():
        result += word + " " if word not in dictionary\
            else dictionary[word] + " "
    return result.strip()


if __name__ == "__main__":
    dictionary = {}
    n = int(input("Enter the count of word pairs: "))
    for _ in range(n):
        ru_word, en_word = map(str, input().split())
        dictionary[ru_word] = en_word
    phrase = input('Enter the phrase to translate: ')
    
    print(translate(phrase, dictionary))
