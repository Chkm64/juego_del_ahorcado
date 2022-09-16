import os
import random

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def get_word():
    words = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(normalize(line.replace("\n", "").upper()))
    return random.choice(words)

def run():
    word = list(get_word())
    letter = ""
    find_letters = []
    while True:
        os.system("cls")
        remaining_letters = ""
        print("Adivina la palabra")
        for i in word:
            aux_find = False
            for j in find_letters:
                if j == i:
                    remaining_letters += f"{j} "
                    aux_find = True
                    break
            #else:
            if not aux_find:
                remaining_letters += "_ "
        print(remaining_letters)
        try:
            if remaining_letters.index("_") >= 0:
                pass
        except Exception as e:
            result = "".join(word)
            os.system("cls")
            print(f"¡Ganaste! La palabra es {result}")
            break
        letter = input('Ingresa un carácter: ').upper()
        try:
            if word.index(letter) >= 0:
                find_letters.append(letter)
        except Exception as e:
            pass


if __name__ == "__main__":
    run()
