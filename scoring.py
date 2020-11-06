from letters import Letters

class Scores(Letters):
    def __init__(self):
        super().__init__()
        self.word=input("Please enter your word: ").lower()
        self.score=0

    def scores(self):
        for l in self.word:
            if l in self.one_point:
                self.score+=1
            elif l in self.two_points:
                self.score+=2
            elif l in self.three_points:
                self.score += 3
            elif l in self.four_points:
                self.score += 4
            elif l in self.five_points:
                self.score += 5
            elif l in self.eight_points:
                self.score += 8
            elif l in self.ten_points:
                self.score += 10
        return self.score



test=Scores()
print(test.scores())