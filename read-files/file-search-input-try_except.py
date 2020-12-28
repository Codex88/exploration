
filename = input("Enter the file name: ")
try:
    filehandle = open(filename)
except:
    print("Bad filename. File cannot be opened.")
    quit()

count = 0
for line in filehandle:
    if line.startswith("Subject:"):
        count += 1
print("There were", count, "subject lines in", filename, ".")
