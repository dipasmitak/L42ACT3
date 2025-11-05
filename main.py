print("Customise your Ride")

print("Select your ride category: ")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    print("\n You selected Bike.")
    print("Choose your type:")
    print("1. Sports Bike")
    print("2. Electric Bike")
    sub_choice = int(input("Enter your choice (1 or 2): "))
    if sub_choice == 1:
        print("You selected Sports 🏍️")
    else:
        print("You selected Electric Bike ⚡🏍️")

elif choice == 2:
    print("\n You selected Car.")
    print("Choose your type:")
    print("1. SUV")
    print("2. Sedan")
    sub_choice = int(input("Enter your choice (1 or 2): "))
    if sub_choice == 1:
        print("You selected SUV 🚙")    
    else:
        print("You selected Sedan 🚗")

else:
    print("Invalid choice! Please select 1 or 2.")
