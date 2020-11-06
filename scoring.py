# Import the letters class
from letters import Letters

# Create a Scores class which is a child of Letters
class Scores(Letters):
    def __init__(self):
        # Use super to inherit from parent class
        super().__init__()
        # Ask user to input their word
        self.word=input("Please enter your word: ").lower()
        # Set score counter to 0
        self.score=0

    def scores(self):
        # For each letter in the word
        for l in self.word:
            # If the letter is in the one_point list, add 1 to the score
            if l in self.one_point:
                self.score+=1
            # If the letter is in the two_point list, add 2 to the score
            elif l in self.two_points:
                self.score+=2
            # If the letter is in the three_point list, add 3 to the score
            elif l in self.three_points:
                self.score += 3
            # If the letter is in the four_point list, add 4 to the score
            elif l in self.four_points:
                self.score += 4
            # If the letter is in the five_point list, add 5 to the score
            elif l in self.five_points:
                self.score += 5
            # If the letter is in the eight_point list, add 8 to the score
            elif l in self.eight_points:
                self.score += 8
            # If the letter is in the ten_point list, add 10 to the score
            elif l in self.ten_points:
                self.score += 10
        # Return a statement telling them their score.
        return "Your score is {}!".format(self.score)

