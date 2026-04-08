# Python Compound interest calculator

principle = 0
rate = 0
time = 0 

while principle <= 0:
    principle = float(input("Enter Amount of principle: "))
    if principle < 0:
        print("Enter Amount Correctly!")

while rate <= 0:
    rate = float(input("Enter Amount of rate: "))
    if rate < 0:
        print("Enter Amount Correctly!")

while time <= 0:
    time = float(input("Enter Amount of time: "))
    if time < 0:
        print("Enter Amount Correctly!")


rumus = principle * (1 + rate / 100), time

print(rumus)