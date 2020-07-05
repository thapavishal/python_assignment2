def is_prime():
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                print("False")
                break
        else:
            print("True")


num = int(input("Enter any positive number: "))
is_prime()
