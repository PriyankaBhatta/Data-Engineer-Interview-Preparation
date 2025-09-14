#python interest compound calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle<0:
        print("Principle cant be less than 0")
    else:
        break

while True:
    rate = float(input("Enter the interest amount: "))
    if rate<0:
        print("Interest cant be less than 0")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time<0:
        print("Time cant be less than 0")
    else:
        break

total_amount = principle * pow((1+rate/100),time)
print(f"Balance after {time} year/s is: {total_amount} ")
