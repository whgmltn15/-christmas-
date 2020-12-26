print(" "*10+"★")
for i in range(1,11):
    for j in range(11-i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
print(" "*9 + "III")
print(" "*3 + "MERRY CHRISTMAS!")