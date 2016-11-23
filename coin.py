import random
h=0
t=0
tog=''
for num in range(1,5001):
    random_num = random.random()
    if random_num <.5:
        h+=1
        tog='heads'
    else:
        t+=1
        tog='tails'
    print "Attempt #" + str(num) + ": Throwing a coin... It's a " + tog + "! ... Got " + str(h) + " heads so far and " + str(t) + " tails so far."
print 'end program'
