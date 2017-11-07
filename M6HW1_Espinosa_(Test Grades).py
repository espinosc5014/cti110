# CTI-110
# M6HW1_Espinosa_(Test Grades)
# Christopher Espinosa
# 11-6-2017
#

def main():
    test1 = float(input("Please enter the first test grade: "))
    test2 = float(input("Please enter the second test grade: "))
    test3 = float(input("Please enter the third test grade: "))
    test4 = float(input("Please enter the fourth test grade: "))
    test5 = float(input("Please enter the fifth test grade: "))
    grade = determine_grade(test1)  
    print(test1,"\t",grade)
    grade = determine_grade(test2)  
    print(test2,"\t",grade)
    grade = determine_grade(test3)  
    print(test3,"\t",grade)
    grade = determine_grade(test4)  
    print(test4,"\t",grade)
    grade = determine_grade(test5)  
    print(test5,"\t",grade)
    average = calc_average(test1,test2,test3,test4,test5)
    grade = determine_grade(average)
    print("Your average score is",average,", your letter grade is",grade)
    

def calc_average(test1,test2,test3,test4,test5):
    total = test1 + test2 + test3 + test4 + test5
    average = total / 5
    return average

def determine_grade(test):
    if test >= 90:
        grade = "A"
        return grade
    elif test <= 89 and test >=80:
        grade = "B"
        return grade
    elif test <= 79 and test >=70:
        grade = "C"
        return grade
    elif test <= 69 and test >=60:
        grade = "D"
        return grade
    else:
        grade = "F"
        return grade

main()

input("\nPress Enter to Exit")
