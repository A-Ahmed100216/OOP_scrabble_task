from letters import Letters

class Scores(Letters):
    def __init__(self,word):
        super().__init__(word)
        self.word=word
        self.score=0

    def one_point_letters(self,word):
        if self.letters == self.word:
            return self.score+1


test=Scores("abc")
print(test.one_point_letters("abc"))