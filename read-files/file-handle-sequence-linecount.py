
filevar = open("./sample-files/mbox-short.txt", encoding="utf-8")
count = 0

for line in filevar:
    count += 1
print(count)
