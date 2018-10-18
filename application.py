# Connor Deardorff
# DevPSU Project 4


# --Helper Function piggify--
# Translates a given word to pig latin
def piggify(word):
    # Get rid of newline character from file, if present
    word = word.strip('\n')

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    # Find if word starts with a vowel
    if word[0] in vowels:
        # Starts with vowel, return word plus "yay"
        return word + "yay";
    else:
        # Starts with consonant, so manipulate the word
        first_vowel = 0
        while word[first_vowel] not in vowels:
            first_vowel += 1

        new_word = word[first_vowel]
        for index in range(first_vowel + 1, len(word)):
            new_word += word[index]

        for index in range(0, first_vowel):
            new_word += word[index]

        return new_word + "ay"
# --End piggify--


# --Main function--
# FILENAME: Path and name of file to be read
filename = "sample_text"

# Open file
file = open(filename)

# Read each line of the file individually
for text in file:
    # Split words apart
    words = text.split(" ")

    # Translate each word into pig latin
    for i in range(0, len(words)):
        words[i] = piggify(words[i])

    # Print translated words
    for word in words:
        print(word, end=' ')
    print('')
    for i in range(0, len(words) - 1):
        word = words[i]
        words[i] = word.strip('\n')
    print(words)

# Close the file
file.close()
# --End main function--
