# CTI-110
# M5HW2_Espinosa_(running total)
# Christopher Espinosa
# 10-12-2017
#


def main():

# Variables
    total = 0
    number = 0

# While Loop    
    while number >= 0:
        number = int(input("Enter number grade: "))
        if number >= 0:
            total = total + number
        else:
            print("Total: ",total)

main()
input("\nPress Enter to Exit")
