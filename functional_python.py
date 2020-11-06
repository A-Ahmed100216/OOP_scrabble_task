# Tackled the problem first using fucntional python
# Created a function called scores
def scores():
    # Take a user input for the word and convert to lower case
    word = input("Please enter your word: ").lower()
    # defined the points allocated for each letter as per the specification.
    one_point= ['a','e','i','o','u','l','n','r','s','t']
    two_points=['d','g']
    three_points=['b','c','m','p']
    four_points=['f','h','v','w','y']
    five_points=['k']
    eight_points=['j','x']
    ten_points=['q','z']
    # set the score counter to 0
    score = 0
    # For each letter in the word, if the letter is present in the point lists, the corresponding points will be added to the score counter.
    for l in word:
        if l in one_point:
            score+= 1
        elif l in two_points:
            score+=2
        elif l in three_points:
            score+= 3
        elif l in four_points:
            score+= 4
        elif l in five_points:
            score+= 5
        elif l in eight_points:
            score+= 8
        elif l in ten_points:
            score +=10
    # The final score is returned
    return score

# Call the function and print to the console.
print(scores())


