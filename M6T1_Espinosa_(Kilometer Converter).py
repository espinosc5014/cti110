# CTI-110
# M6T1_Espinosa_(Kilometer Converter)
# Christopher Espinosa
# 10-26-2017
#

def show_miles(km):
    miles = km * 0.6214
    print(km,"kilometers is equal to", miles,"miles")
          
def main():
    print("This programs converts Kilometers to Miles.")
    kilometers = float(input("Please enter a distance in Kilometers: "))
    show_miles(kilometers)


main()

input("\nPress Enter to Exit")
