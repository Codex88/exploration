# Takes input file from end-user and produces final word counts

filename = input("Enter a filepath: ")

# failsafe for bad filepath
try:
    filehandle = open(filename)
except:
    print("Bad filepath. Cannot open file.")
    quit()

# declare dictionary
word_count = dict()

# parse words from file
for line in filehandle:
    words = line.split()
    for word in words:
        word = word.removesuffix(".")
        word_count[word] = word_count.get(word, 0) + 1

# count words
most_used_word = None
frequency = None
for word, count in word_count.items():
    if frequency is None or count > frequency:
        most_used_word = word
        frequency = count

# sort & print word count dictionary
print("\nWord Dictionary:\n")
for k, v in sorted(word_count.items()):
    print(k, v)

# print most used word and counted frequency
print("\nThe most used word was:", most_used_word)
print("Frequency:", frequency, "iterations")
