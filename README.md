# Task - Scrabble Word Calculator

### Summary
In Scrabble, different letters have different values dependant on how hard it is to incorporate the letter into a word. Create a simple calculator which can calculate the score of a word. 

### Task
1. Use the table below to create a Scrabble word calculator that will provide the correct scores dependent on the string provided. 

```text
Letter                             Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
```

### Acceptance Criteria

* Completes required tasks
* Create a new project and repository
* Have at least 5 commits
* Include documentation
* Follow best practices

# Process 
##### Preliminary 
*This task was approached by first solving via functional python and then applying object oriented programming. The functional code is as follows:*
```python
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
```

#### 1. Create a Parent class
* The parent class in this task is defined as Letters. 
* The class is initialised and attributes created of points possible. 
```python
# Create a letter class to hold the score of each letter
class Letters:
    def __init__(self):
        self.letters=['a','b','c','d']
        self.one_point = ['a', 'e', 'i', 'o', 'u', 'l', 'n', 'r', 's', 't']
        self.two_points = ['d', 'g']
        self.three_points = ['b', 'c', 'm', 'p']
        self.four_points = ['f', 'h', 'v', 'w', 'y']
        self.five_points = ['k']
        self.eight_points = ['j', 'x']
        self.ten_points = ['q', 'z']
```
#### 2. Create a Child class 
* The Scores class is a child of the Letters class. Thus, Letters must be imported. 
```python
from letters import Letters
```
* The initialisation function takes an input from the user which is the word which they wish to score. This is converted to lower case so as to match the format of the scoring system. 
* Also during initislaistion, the score is set to 0. 

```python
class Scores(Letters):
    def __init__(self):
        super().__init__()
        self.word=input("Please enter your word: ").lower()
        self.score=0
```

* The scores function is defined. This takes each character in the input string and evaluates whether it appears in the list attributes created in the Parent class 
```python
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
        return "Your score is {}!".format(self.score)
```
#### 3. Instantiation
* A test file is used to create an instance and run the code.
* The Letters and Scores classes are both imported. 
```python
from letters import Letters
from scoring import Scores
```
* An object/instance of the Score class is created.
* The scores function is executed and the result printed. 
```python
scrabble_test=Scores()
print(scrabble_test.scores())
```
 
 


