import random
class FruitQuiz:
    def __init__ (self):
        self.fruits = {'apple':'red', 'banana':'yellow', 'grape':'purple', 'orange':'orange', 'kiwi':'brown'}
    def quiz (self):
        while True:
            fruit, colour = random.choice(list(self.fruits.items()))
            print("What is the colour of a ", fruit, "?")
            answer = input("Your answer: ")
            if answer.lower() == colour:
                print("Correct!")
            else:
                print("Incorrect! The correct answer is", colour)
            cont = input("Do you want to continue? (y/n): ")
            if cont.lower() != 'y':
                break 

print("Welcome to the Fruit Colour Quiz!")
quiz = FruitQuiz()
quiz.quiz()
