# Triangle type checker

a = int(input("Enter side 1"))
b = int(input("Enter side 2"))
c = int(input("Enter side 3"))
if a == b == c:
    print("Equirateral")
elif a == b and   a != c:
    print("isosceles")
elif a !=b and a !=c and b !=c:
    print("Scalene")