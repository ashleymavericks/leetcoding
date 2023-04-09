import random

grid = 4
max_point = grid * grid

player_dict = {}
history = [[], [], [], []]
dice_history = [[], [], [], []]

while(max_point not in player_dict.values()):
    for i in range(4):
        dice_roll = random.randint(1, 6)
        dict_values = player_dict.values()
        if max_point in dict_values:
            break
        dice_history[i].append(dice_roll)

        if history[i]:
            new_score = history[i][-1] + dice_roll
            if new_score <= max_point:
                history[i].append(new_score)
                player_dict[i] = new_score
            else:
                history[i].append(history[i][-1])
        elif dice_roll <= max_point:
            history[i].append(dice_roll)
            player_dict[i] = dice_roll


for i in range(len(history)):
    win_status = 1 if player_dict[i] == max_point else 0
    print(
        f"Dice Roll History: {dice_history[i]} | Player {i+1}: {history[i]} | Win Status: {win_status}")
