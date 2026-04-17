import random

print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

"┌──────────┐"
"│          │"
"│          │"
"│          │"
"└──────────┘"

dice_number = {
    1 : ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"
         ),
    2 : ("┌─────────┐",
         "│  ●      │",
         "│         │",
         "│      ●  │",
         "└─────────┘"
         ),
    3 : ("┌─────────┐",
         "│  ●      │",
         "│    ●    │",
         "│      ●  │",
         "└─────────┘"
         ),
    4 : ("┌─────────┐",
         "│  ●   ●  │",
         "│         │",
         "│  ●   ●  │",
         "└─────────┘"
         ),
    5 : ("┌─────────┐",
         "│  ●   ●  │",
         "│    ●    │",
         "│  ●   ●  │",
         "└─────────┘"
         ),
    6 : ("┌─────────┐",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "│  ●   ●  │",
         "└─────────┘"
         ),
}

dice = []
total = 0
number_of_dice = int(input("Enter number of dice: "))

if number_of_dice not in dice_number.keys():
    print('Pastikan sama dengan', dice_number.keys)

for dice_range in range(number_of_dice):
    dice.append(random.randint(1, 6))

for dice_line in range(number_of_dice):
    for line in dice_number.get(dice[dice_line]):
        print(line)

for dice in dice:
    total += dice

print(f"Total {total}")