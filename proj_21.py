# игра 21 очко

import random
import time

class Player:
    def __init__(self, score=0, drop=None, flag=True) -> None:
        self.score = score
        self.drop = drop
        self.flag = flag

user = Player()
computer = Player()
n = 1

print("Добро пожаловать в игру 21!")
time.sleep(n)
print("Бросайте кубик до тех пор, пока не приблизитесь к 21, потом настанет очередь вашего соперника.")

while user.flag and user.score < 21:
    time.sleep(n)
    print("Ты хочешь бросить кубик? YES/NO")
    answer = input().lower()
    if answer == "yes":
        user.drop = random.randint(1, 11)
        time.sleep(n)
        print(f"Тебе выпало: {user.drop}")
        user.score += user.drop
    elif answer == "no":
        user.flag = False
        time.sleep(n)
        print("Хорошо!")
    else:
        print("Ты написал не правильно, поробуй ещё.")
    time.sleep(n)
    print(f"Твой текущий счёт: {user.score}")
    if user.score == 21:
        time.sleep(n)
        print("Поздравляю, ровно 21!")
    elif user.score > 21:
        time.sleep(n)
        print("Как жаль! Ты перебрал!")

time.sleep(n)
print("Очередь соперника бросать кубик!")
while computer.score < 16:
    time.sleep(n)
    print("Соперник ещё раз бросает кубик...")
    computer.drop = random.randint(1, 11)
    computer.score += computer.drop
    time.sleep(n)
    print(f"Твоему сопернику выпало {computer.drop}\nЕго текущий счёт: {computer.score}")

time.sleep(n)
print("Итак... Победитель...")

if user.score <= 21 and (computer.score > 21 or computer.score < user.score):
    time.sleep(n)
    print(f"Ты выиграл со счетом: {user.score}")
elif user.score > 21 and (computer.score <= 21 or user.score < computer.score):
    time.sleep(n)
    print(f"Выиграл твой соперник! Он набрал: {computer.score}")
else:
    time.sleep(n)
    print("Поздравляю! У вас ничья!")


