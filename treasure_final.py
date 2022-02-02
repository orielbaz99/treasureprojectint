import random

treasure_path = r"C:\Users\97254\Desktop\test\treasureProject.txt"

start = ''
end = ''

with open(treasure_path, 'w') as file1:
    for i in range(1, 10):
        start += str(i) * (random.randint(1, 20))  # creates the first part of the text

    for i in range(9, 0, -1):
        end += str(i) * (random.randint(1, 20))  ##creates the second part of the text

    file1.write(start + 'TREASURE' + end)

playing = True

with open(treasure_path, 'r') as file1:
    s = 0  # pointer starting position
    tries = 0
    while playing:

        DIRECTION = int(input('What direction would you like to move? [1-forward 2-backwards]\n'))

        if DIRECTION == 1:
            movement = int(input('How many steps?\n'))
            s += movement
            tries += 1
            file1.seek(s - 1)
            print(f'you hit * {file1.read(1)} *\n')

            if file1.read(1) in 'TREASURE':
                playing = False
                print('**** YOU FOUND THE TREASURE ****\n')
                print(f'It took you {tries} tries\n')

        elif DIRECTION == 2:
            movement = int(input('How many steps?\n'))
            s -= movement
            tries += 1
            file1.seek(s - 1)
            print(f'you hit * {file1.read(1)} *\n')

            if file1.read(1) in 'TREASURE':
                playing = False
                print('**** YOU FOUND THE TREASURE ****\n')
                print(f'It took you {tries} tries\n')
        else:
            print('wrong input try again\n')
