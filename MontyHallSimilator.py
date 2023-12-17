import random

correct_by_staying = 0
correct_by_changing = 0
for choose in range(1000):
    guess = random.randint(1, 3)
    prize = random.randint(1, 3)
    doors = [1, 2, 3]
    doors.remove(guess)
    if guess != prize:
        doors.remove(prize)
    player_choose = random.choice(doors)
    # print("player_choose door: ", player_choose)
    if guess == prize:
        correct_by_staying += 1
    else:
        correct_by_changing += 1
print("of correct by staying: ", correct_by_staying)
print("of correct by changing: ", correct_by_changing)
