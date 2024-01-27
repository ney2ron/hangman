

stages = ["",
          "--------------",
          "|      |      ",
          "|      0      ",
          "|     /X\\    ",
          "|     / \\    ",
          "|             ",
          ]
max_wrong = len(stages) - 1
words = {"КОТ":"кто ловит мышей",
         "КРОТ":"у кого жила дюймовочка под землей",
         "КОМПЬЮТЕР":"вычислительная машина, в которую можно играть",
         "КРЫСА":"самый живучий обитатель канализации"}
import random
import os
key = random.choice(list(words.keys()))
length = "_" * len(key)
wrong = 0 
used = []
while wrong < max_wrong and length!=key:
    print("Добро пожаловать на казнь!")
    print("Отгадай слово и спаси висильника")
    print("Подсказака: \n\t",words[key])
    print("Вы предлогали такие буквы", used)
    print("Отгаданное вами слово сейчас выглядит так:",length,"\n")
    guess = input("Введите букву: ")
    guess = guess.upper()
    while guess in used:
        print("Вы уже вводили букву: ",guess)
        guess = input("Введите другую букву: ")
        guess = guess.upper()
    used.append(guess)
    if guess in key:
        print("Умница буква",guess,"есть в слове:")
        new = ""
        for i in range(len(key)):
            if guess == key[i]:
                new += guess
            else:
                new += length[i]
        length = new
    else:
        print("К сожалению",guess,"нет в слове.")
        wrong += 1
        e = wrong + 1 
        print("\n".join(stages[0:e]))
    
    os.system("cls")
if wrong == max_wrong:
    print(" Вас повесили :( ")
    print(stages[wrong])
else:
    print("Победа! Ты спасся")
    print("Ты предлогал следующие буквы",used)
    print("Отгаданное слово выглядит так",length,"\n")
    print("Загаданное было слово", key)
    print("Чтобы выйти нажми Enter")
