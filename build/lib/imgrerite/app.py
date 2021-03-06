# importing libraries
import os
from pathlib import Path

# defining ANSI escape codes
TGREEN = '\033[32m'
TRED = '\033[31m'
TYELLOW = '\033[33m'
TITALIC = '\033[3m'
ENDC = '\033[m'

# welcome banner
welcomeText = (""" /$$$$$$                               /$$$$$$$                  /$$$$$$$  /$$   /$$              
|_  $$_/                              | $$__  $$                | $$__  $$|__/  | $$              
  | $$   /$$$$$$/$$$$   /$$$$$$       | $$  \ $$  /$$$$$$       | $$  \ $$ /$$ /$$$$$$    /$$$$$$ 
  | $$  | $$_  $$_  $$ /$$__  $$      | $$$$$$$/ /$$__  $$      | $$$$$$$/| $$|_  $$_/   /$$__  $$
  | $$  | $$ \ $$ \ $$| $$  \ $$      | $$__  $$| $$$$$$$$      | $$__  $$| $$  | $$    | $$$$$$$$
  | $$  | $$ | $$ | $$| $$  | $$      | $$  \ $$| $$_____/      | $$  \ $$| $$  | $$ /$$| $$_____/
 /$$$$$$| $$ | $$ | $$|  $$$$$$$      | $$  | $$|  $$$$$$$      | $$  | $$| $$  |  $$$$/|  $$$$$$$
|______/|__/ |__/ |__/ \____  $$      |__/  |__/ \_______/      |__/  |__/|__/   \___/   \_______/
                       /$$  \ $$                                                                  
                      |  $$$$$$/                                                                  
                       \______/                                                                   """)
print(f'\n{TRED}{welcomeText}{ENDC}')

# checking for user input
flag1 = False

while not flag1:

    print(f'Choose from one of the options below: ')
    print(f'\n{TGREEN}[H] for hiding text in image{ENDC}')
    print(f'{TGREEN}[R] for revealing any hidden text in the image{ENDC}')
    print(f'{TRED}[Q] for quitting{ENDC}')
    choice = input(f"\n{TGREEN}> {ENDC}")

    if choice == 'H' or choice == 'h' or choice == 'R' or choice == 'r' or choice == 'Q' or choice == 'q':
        flag1 = True

# logic of the app

# quits the program
if choice == 'Q' or choice == 'q':

    print(f'\n{TYELLOW}Thanks for using Imgrerite <3{ENDC}\n')

# hides the text
elif choice == 'H' or choice == 'h':
    flag2 = False

    while not flag2:

        try:
            img1 = input('\nImage path: ')
            ext1 = img1[len(img1) - 3: len(img1)]
            with open(img1, 'rb') as file1:
                con1 = file1.read()

            text = input('\nEnter the text to be hidden: ')
            fname = input('\nSave encrypted image as: ')

            directory = f'{Path.home()}/Imgrerite'
            if os.path.isdir(directory) == False:
                os.mkdir(directory, 0o666)
            output = f'{directory}/{fname}.{ext1}'

            with open(output, 'wb') as file2:
                t = con1 + bytes(text, 'utf-8')
                file2.write(t)

            flag2 = True

            print(f'\n{TYELLOW}Text successfully hidden, thanks for using Imgrerite <3{ENDC}')

        except:
            print(f'{TRED}Please, enter the correct image path!{ENDC}')

# reveals the hidden texts
elif choice == 'R' or choice == 'r':
    flag = False

    while not flag:

        try:
            img2 = input('\nImage path: ')
            ext2 = img2[len(img2) - 3: len(img2)]
            with open(img2, 'rb') as file3:
                con2 = file3.read()

                if ext2 == 'png':
                    offset = con2.index(bytes.fromhex('42 60 82'))
                    file3.seek(offset + 3)

                elif ext2 == 'jpg':
                    offset = con2.index(bytes.fromhex('FFD9'))
                    file3.seek(offset + 2)

                p = file3.read()
                print(f'\nHidden text: ', end=' ')
                print(f'{TGREEN}{TITALIC}{p.decode()}{ENDC}')

            flag = True

            print(f'\n{TYELLOW}Thanks for using Imgrerite <3{ENDC}')

        except:
            print(f'{TRED}Please, enter the correct image path!{ENDC}')