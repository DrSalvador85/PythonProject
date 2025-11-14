def foundLetterInWord(word, letter):
    """Count how many times a letter appears in a word (case-insensitive)."""
    word = word.lower()
    letter = letter.lower()
    howMany = 0
    for thisLetter in word:
        if thisLetter == letter:
            howMany += 1
    return howMany

def main():
    userWord = input('Enter a word: ').lower()
    userLetter = input('Enter a letter: ').lower()
    result = foundLetterInWord(userWord, userLetter)
    print(f"The letter '{userLetter}' appears {result} time(s) in '{userWord}'.")


if __name__ == "__main__":
    main()
