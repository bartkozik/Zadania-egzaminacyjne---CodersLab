import random


def roll(dice_num, modi, dice_type=6):
    possible_dice = [3,4,6,8,10,12,100]
    if dice_type in possible_dice:
        return dice_num*random.randint(1, dice_type) + modi
    else:
        raise Exception('No such dice!')

print(roll(2, 20, 10))