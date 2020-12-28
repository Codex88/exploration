# open the file wrapper
filevar = open("./sample-files/mbox-short.txt", encoding="utf-8")
# read the file as a variable & print the length
count = filevar.read()
print(len(count))

# print first 20 characters
print(count[:20])
