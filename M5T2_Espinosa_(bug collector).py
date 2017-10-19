# CTI-110
# M5T2_Espinosa_(bug collector)
# Christopher Espinosa
# 10-12-2017
#

def main():

# Variables
    day = (1,2,3,4,5,6,7)
    bugs_today = int("0")
    bugs_total = int("0")

# For Loop
    for number in day:
        print("Day",number)
        bugs_today = int(input("Number of bugs caught today? "))
        bugs_total += bugs_today

# Display Bug Total
    print("\nYou have caught a total of",bugs_total,"bugs this week.")

# Feedback
    if bugs_total <= 7:
        print("\nYou need to try harder.")
    else:
        print("\nGreat Job!")
                    

main()

input("\nPress Enter to Exit")
