# CTI-110
# P3Lab Debugging
# Eddie Drake
# 7 Mar 2018


# This program gets a numeric test score from the
# user and display the corresponding letter grade
# Variables to represent the grade thresholds

A_score = 90
B_score = 80
C_score = 70
D_score = 60

def main():
    

    score = int (input ("Enter your test score? "))

    if score >= A_score:
        print ("Your grade is A,")

    else:
        if score >= B_score:
            print ("Your grade is B. ")

        else:
            if score >= C_score:
                print ("Your grade is C. ")

            else:
                if score >= D_score:
                    print ("Your grade is D. ")
                else:
                    print ("Your grade is F. ")

main()
