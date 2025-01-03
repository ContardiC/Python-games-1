word = "casa"
word_length = len(word)

def print_underscore(word):
    for character in word:
        print("_", end="")
print(f"The word {word} is {word_length} characters long  ")
print_underscore(word)
