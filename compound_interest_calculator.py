name = ""
princeple = 0
interest = 0
time = 0

while True:
    name = input("Enter your name : ")
    if name == "":
        print("Please enter your name")
    else:
        break

while True:
    princeple = float(input("Enter the Principle amount : "))
    if princeple <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    interest = float(input("Enter the Interest Rate : "))
    if interest <= 0:
        print("Interest Rate can't be less than or equal to zero")
    else:
        break

while True:
    time = int(input("Enter the time in years : "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

total = princeple * pow((1 + interest / 100), time)
print(f"Hello {name.title()} your balance after {time}years : ${total:.2f}")

