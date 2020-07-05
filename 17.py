def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    mul = a*b
    return mul


def divide(a, b):
    div = a/b
    return div


print("Make a choice: ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter your choice: ")


x = int(input("Enter num 1: "))
y = int(input("Enter num 2: "))

if choice == '1':
    print("The sum is: ", add(x, y))

elif choice == '2':
    print("The diff is: ", subtract(x, y))


elif choice == '3':
    print("The mul is: ", multiply(x, y))


elif choice == '4':
    print("The div is: ", divide(x, y))


else:
    print("Invalid choice")
