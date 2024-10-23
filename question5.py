# Simple Age checker

# age is less or equal to 18 (minor)
# age is >18 and <= 65 (Adult)
# age is >65 (senior)
age = int(input("Enter your age: "))

if age <= 18 :
    print("Minor")
elif age> 18  <= 65:
    print("Adult")
elif age> 65:
    print("Senior")

