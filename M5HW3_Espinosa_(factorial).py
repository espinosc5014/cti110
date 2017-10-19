# CTI-110
# M5HW3_Espinosa_(factorial)
# Christopher Espinosa
# 10-12-2017
#


def main():

    number = int("0")
    total = int("1")

    number = int(input("Enter a nonnegative number: "))
    factorial = range(number,0,-1)

    for n in factorial:
        total *= n 
        print(n)

    print("\nThe Facttorial of",number,"is",total)

main()
input("\nPress Enter to Exit")
