
def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores (between 0 and 5) into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating
    
def convert_to_numeric(x):
    return float(x)

def sum_of_middle_three(a,s,d,f,g):
    return (a+s+d+f+g)-min(a,s,d,f,g)-max(a,s,d,f,g)
    
def score_to_rating_string(y):
    if 0<=y<1:
        return 'terrible' #or you could just do print('terrible')
    elif 1<=y<2:
        return 'bad'
    elif 2<=y<3:
        return 'ok'
    elif 3<=y<4:
        return 'good'
    elif 4<=y<=5:
        return 'excellent'

#if youre printing the output in the function score_to_rating_string, 
#you dont need this part
print(scores_to_rating(3,3,"2",4,1.0))
