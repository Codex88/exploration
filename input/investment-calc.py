principle = float(input("Enter the principle: "))
APY = float(input("Enter the APY (in decimal): "))
period = int(input("Enter the number of years: "))
value = 0
year = 1
while year <= period:
    value = principle + (APY * principle)
    print(f"Year {year}: ${value} USD")
    principle = value
    year = year + 1
