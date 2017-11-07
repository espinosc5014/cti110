# CTI-110
# M6T2_Espinosa_(Feet to Inches Converter)
# Christopher Espinosa
# 10-26-2017
#

def main():
    print("This program converts feet to inches.")
    feet = float(input("\nPlease input a distance in feet: "))
    inches = feet_to_inches(feet)
    print(feet,"feet is equal to",inches,"inches.")
    
def feet_to_inches(ft):
    inches = ft * 12
    return inches
    
main()

input("\nPress Enter to Exit")
