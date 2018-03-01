# CTI-110
# P3HW1-Age Classifier
# Eddie Drake
# 1 Mar 2018

age = int (input ("What is the individual's age? " ))

if age <= 1:
    print ("infant")
elif age < 13:
    print ("child")
elif age < 20:
    print ("teenager")
else:
    print ("adult")
    
