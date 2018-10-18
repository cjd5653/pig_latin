# Connor Deardorff
# DevPSU Project 4

# --Main function--
# FILENAME: Path and name of file to be read
filename = "sample_text"

# Open file
file = open(filename)

# Read each line of the file individually
for text in file:
    # Split words apart
    words = text.split(" ")
    for i in range(0, len(words) - 1):
        word = words[i]
        words[i] = word.strip('\n')
    print(words)

# Close the file
file.close()
# --End main function--
