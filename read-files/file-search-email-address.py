filename = input("Enter the filepath: ")
try:
    filehandle = open(filename, encoding="utf-8")
except:
    print("Bad filepath. Cannot open file.")
    quit()

for line in filehandle:
    line = line.rstrip()
    if line.startswith("From:"):
        emaillist = line.split(" ")
        email = emaillist[1]
        print(email)
