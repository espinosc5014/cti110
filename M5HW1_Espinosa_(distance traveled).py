# CTI-110
# M5HW1_Espinosa_(distance traveled)
# Christopher Espinosa
# 10-12-2017
#

def main():

# Variables
    speed = int(input("What is the speed of the vehicle in mph? "))
    hours = int(input("How many hours has it traveled? "))
        
# Display
    print("""
Hour\t\tDistance Traveled
----------------------------------
""")
    travel = range(1,hours + 1)

    for number in travel:
        distance = speed * number
        print(number,"\t\t",distance,"miles")


main()
input("\nPress Enter to Exit")
