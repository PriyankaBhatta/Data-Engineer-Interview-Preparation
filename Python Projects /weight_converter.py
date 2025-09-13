#python weight converter program ks-> pounds and vice versa

weight = float(input("Enter you weight: "))
unit = input("Kilograms or pounds (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight,1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kg"
    print(f"Your weight is {round(weight,1)} {unit}")
else:
    print(f" {unit} is not valid.")
