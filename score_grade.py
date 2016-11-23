print "Scores and Grades"
print "Please enter your test score:"

for num in range(0,10):
    score = input()
    if score<60:
        grade='F'
        print 'With a score of '+ str(score) +' your grade is ' + grade + '.'
    elif score>=60 and score<70:
        grade='D'
        print 'With a score of '+ str(score) +' your grade is ' + grade + '.'
    elif score>=70 and score<80:
        grade='C'
        print 'With a score of '+ str(score) +' your grade is ' + grade + '.'
    elif score>=80 and score<90:
        grade='B'
        print 'With a score of '+ str(score) +' your grade is ' + grade + '.'
    elif score>=90 and score<=100:
        grade='A'
        print 'With a score of '+ str(score) +' your grade is ' + grade + '.'
    else:
        print "Please enter a score between 1 and 100"
