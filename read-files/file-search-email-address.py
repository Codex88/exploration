filename = input("Enter the filepath: ")
try:
    filehandle = open(filename, encoding="utf-8")
except:
    print("Bad filepath. Cannot open file.")
    quit()

for line in filename:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
