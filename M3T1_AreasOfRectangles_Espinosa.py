#CTI-110
#M3T1_AreasOfRectangles_Espinosa.py
#Christopher Espinosa
#09-07-2017

rectangle_1_length = int(input("What is the length of the first rectangle?  "))
rectangle_1_width = int(input("What is the width of the first rectangle?  "))
rectangle_2_length = int(input("What is the length of the second rectangle?  "))
rectangle_2_width = int(input("What is the width of the second rectangle?  "))
rectangle_1_area = rectangle_1_length * rectangle_1_width
rectangle_2_area = rectangle_2_length * rectangle_2_width

print(rectangle_1_length, "x",rectangle_1_width, "=",rectangle_1_area, "area.")
print(rectangle_2_length, "x",rectangle_2_width, "=",rectangle_2_area, "area.")

if rectangle_1_area > rectangle_2_area:
    print("\nRectangle one has the greater area.")
elif rectangle_1_area < rectangle_2_area:
    print("\nRectangle two has the greater area.")
else:
    print("\nRectangle one and Rectangle two have the same area.")

input("\n\nPress Enter to End Program.")
