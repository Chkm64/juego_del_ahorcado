import os
import random

def normalize(string):
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for a, b in replacements:
        string = string.replace(a, b).replace(a.upper(), b.upper())
    return string

def get_word():
    with open("./data.txt", "r", encoding="utf-8") as f:
        words = [line.replace("\n", "") for line in f]
    return random.choice(words)

def run():
    word = normalize(get_word()).upper()
    search_word = len(word) * "_ "
    while word != search_word.replace(" ", ""):
        os.system("cls")
        print("Adivina la palabra")
        print(search_word)
        letter = normalize(input('Ingresa un carácter: ')).upper()
        if letter in word:
            search_word = list(search_word.replace(" ",""))
            for index, value in enumerate(word):
                if value == letter:
                    search_word[index] = letter
            search_word = " ".join(search_word)
    os.system("cls")
    print(f"¡Ganaste! La palabra es {word}")


if __name__ == "__main__":
    run()
