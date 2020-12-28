filename = open("./sample-files/mbox-short.txt", encoding="utf-8")

for line in filename:
    line = line.rstrip()
    if line.startswith("From:"):
        linelist = line.split()
        emaillist = linelist[1].split("@")
        print(emaillist[1])
