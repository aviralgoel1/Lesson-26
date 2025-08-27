class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__ (self):
        return self.word+'('+self.meaning+')'

flash = []
print ("welcome to flashcard app")

while True:
    word = input("Enter the name you want to add to flashcard: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(flashcard(word, meaning))
    ch = input("Do you want to add more words? (y/n): ")
    if ch.lower() != 'y':
        break
print("\nYour flashcards:")
for card in flash:
    print(card)