# CTI-110 
# M3HW1 - Age Classifier 
# Chris Espinosa 
# 09-12-2017
#


age = float(input("Please enter your age: "))

infant = 1
child = 12
teenager = 19

if age <= infant:
    print("You are an infant.  How are you using a computer?")
elif age > infant and age <= child:
    print("You are a child.")
elif age > child and age <= teenager:
    print("You are a teenager.")
else:
    print("You are an adult.")

input("\n\nPress Enter to Exit Program")
