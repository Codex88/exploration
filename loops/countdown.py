
timer = input("Enter number to start from: ")


try:
    timer = int(timer)
except:
    print("An exception occurred.")

while timer >= 0:
    print(timer)
    timer = timer - 1
print("BLASTOFF!!")
