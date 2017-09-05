#CTI-110
#M2HW2_TipTaxTotal_Espinosa.py
#Christopher Espinosa
#09/05/2017

subtotal = float(input("What is the bill amount? "))
tax = subtotal * .07
total = subtotal + tax
tip = total * .18
total_bill = total + tip

print("\nSubtotal:\t $", format(subtotal,',.2f'))
print("Tax @ 7%:\t $", format(tax,',.2f'))
print("Total:\t\t $", format(total,',.2f'))
print("Tip @ 18%:\t $", format(tip,',.2f'))
print("Total Amount:\t $", format(total_bill,',.2f'))

input("\n\nPress Enter To Exit.")
