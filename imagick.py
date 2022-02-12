#AUTHOR: Jigyasu

#defining ANSI escape codes
TGREEN = '\033[32m'
TRED = '\033[31m'
TYELLOW = '\033[33m'
TITALIC = '\033[3m'
ENDC = '\033[m'

#welcome banner
welcomeText = ("""  _____                               _          _         _____   _        _____ 
 |_   _|                             (_)        | |       / ____| | |      |_   _|
   | |    _ __ ___     __ _    __ _   _    ___  | | __   | |      | |        | |  
   | |   | '_ ` _ \   / _` |  / _` | | |  / __| | |/ /   | |      | |        | |  
  _| |_  | | | | | | | (_| | | (_| | | | | (__  |   <    | |____  | |____   _| |_ 
 |_____| |_| |_| |_|  \__,_|  \__, | |_|  \___| |_|\_\    \_____| |______| |_____|
                               __/ |                                              
                              |___/                                               """)
print(f'\n{TRED}{welcomeText}{ENDC}')

#checking for user input
flag1 = False

while not flag1:

    print(f'Choose from one of the options below: ')
    print(f'\n{TGREEN}[H] for hiding text in image{ENDC}')
    print(f'{TGREEN}[R] for revealing any hidden text in the image{ENDC}')
    print(f'{TRED}[Q] for quiting{ENDC}')
    choice = input(f"\n{TGREEN}> {ENDC}")

    if choice == 'H' or choice == 'h' or choice == 'R' or choice == 'r' or choice == 'Q' or choice == 'q':
        flag1 = True

#logic of the app

#quits the program
if choice == 'Q' or choice == 'q':

    print(f'\n{TYELLOW}Thanks for using Imagick <3{ENDC}')
    print(f'{TYELLOW}Star this project on GitHub: https://github.com/cheesemaafia/ImagickCLI\n{ENDC}')

#hides the text
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
            output = f'{fname}.{ext1}'
            with open(output, 'wb') as file2:
                t = con1 + bytes(text, 'utf-8')
                file2.write(t)

            flag2 = True

            print(f'\n{TYELLOW}Text successfully hidden, thanks for using Imagick <3{ENDC}')
            print(f'{TYELLOW}Star this project on GitHub: https://github.com/cheesemaafia/ImagickCLI\n{ENDC}')

        except:
            print('Please, enter the correct image path!')

#reveals the hidden texts
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

            print(f'\n{TYELLOW}Thanks for using Imagick <3{ENDC}')
            print(f'{TYELLOW}Star this project on GitHub: https://github.com/cheesemaafia/ImagickCLI\n{ENDC}')

        except:
             print(f'{TRED}Please, enter the correct image path!{ENDC}')
