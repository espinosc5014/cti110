# CTI-110
# M3Lab: Debugging
# Christopher Espinosa
# 09-12-2017

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    # TO DO: define the rest of the scores
    
    score = int(input('Enter grade score: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score <= A_score and score >= B_score:
        print('Your grade is: B')
    elif score <= B_score and score >= C_score:
        print('Your grade is: C')
    elif score <= C_score and score >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')
    # TO DO: finish this

# program start
main()
