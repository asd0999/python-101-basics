#depending on the points, prize is determined

#one way to do this
my_points=50

def which_prize(points):
    if points<=50:
        return 'wooden rabbit'
    elif 50<points<=150:
        return 'no prize'
    elif 150<points<=180:
        return 'wafer-thin mint'
    else:
        150<points<=200
        return 'penguin'

prize = which_prize(my_points)

if prize == 'no prize':
    print("oh dear, no prize this time.")
else:
    print("Congratulations! You have won a {}.".format(prize))


#another way to do this
def which_prize2(points):
    prize = None
    if points<=50:
        prize = 'wooden rabbit'
    elif 150<points<=180:
        prize = 'wafer-thin mint'
    elif 150<points<=200:
        prize = 'penguin'

    if prize:
        print("Congratulations! You have won a {}!".format(prize))
    else:
        print("Oh dear, no prize this time.")
    
#here, the points are mentioned in the parenthesis when calling the function
#you could store in a variable also if you want
which_prize2(194)
