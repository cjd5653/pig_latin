# Connor Deardorff
# DevPSU Project 4

# --Main function--
# FILENAME: Path and name of file to be read
filename = "sample_text"

# Open file
file = open(filename)

# Read each line of the file individually
for text in file:
    print(text)

# Close the file
file.close()
# --End main function--
