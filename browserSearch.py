'''
Author : H34TB14ST
Date   : 25th July 2003
Version 1.1
Description : This little piece of browserSearch file is just for my
              Python scripting practice. So, please don't take this 
              as seriously!
              But if I feel like adding new features, I would.
              Until then, enjoy!
'''

import webbrowser
import colorama
from colorama import Fore,Back,Style
import requests
from pyfiglet import Figlet
colorama.init()

# Just for styling figlet
f = Figlet(font='3d')
print(Back.BLACK+f.renderText('Searchy'))

# Banner
print(Fore.RED+Back.BLACK+'\n+------------------------+')
print('| SEARCH ANYTHING        |')
print('| Developed by H34TB14ST |')
print('| Version 1.1            |')
print('+------------------------+')
#print('\033[39m') # Note for green code, you can try it :))
print(Fore.RESET)
while True:
    # Option numbers list to choose
    print(Fore.RED+Style.BRIGHT+'[1] YouTube search')
    print(f'{Fore.BLUE}[2] G{Fore.RED}o{Fore.YELLOW}o{Fore.BLUE}g{Fore.GREEN}l{Fore.RED}e {Fore.WHITE+Style.BRIGHT}search')
    print(Fore.GREEN+Style.BRIGHT+'[3] Spotify search')
    print(Fore.RESET+Style.BRIGHT+'[4] Lyrics search')
    print('[Q] Exit')
    print('')
    choose = input("Choose one -> ")

    # YouTube search
    if choose == '1':
        print('')
        print('[b] Back')
        search = input('YouTube search -> ')
        print('')
        if search != 'b':
            # Open the system's default web browser and search the input on youtube
            webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
        else:
            continue
    
    # Google search
    elif choose == '2':
        print('')
        print('[b] Back')
        search = input('Google search -> ')
        print('')
        if search != 'b':
            # Open the system's default web browser and search the input on google
            webbrowser.open(f'https://google.com/search?q={search}')
        else:
            continue
    
    # Spotify search
    elif choose == '3':
        print('')
        print('[b] Back')
        search = input('Soptify search -> ')
        print('')
        if search != 'b':
            # Open the system's default web browser and search the input on spotify
            webbrowser.open(f"https://open.spotify.com/search/{search}")
        else:
            continue
    
    # Lyrics search
    elif choose == '4':
        print('')
        print('[b] Back')
        artist = str(input("Enter artist :"))
        if artist != 'b':
            song = str(input(f"Enter a song by {artist.title()} :"))
            try:
                # Make GET request to the lyrics.ovh site
                response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{song}')

                # The responded data is in json format but it showed as str type, so, it is convert into proper 
                # json object
                plain_text = response.json()

                # Then convert it into dict object
                plain_text = dict(plain_text)

                # First line of every resulted lyrics is removed
                frist_line_of_lyrics = f"Paroles de la chanson {song.upper()} par {artist.capitalize()}"
                len_to_ignore = int(len(frist_line_of_lyrics))

                # Out put the final lyrics here :)
                print(plain_text.get('lyrics')[len_to_ignore::],'\n')

            except Exception:
                print(Fore.RED+"Lyrics not found! Please, try again with correct name formats! \n")
        else:
            continue
    
    # Option to Quit the program from running
    elif choose == 'q' or choose == 'Q':
        break

    else:
        print('_________________')
        print('  Choose again! ')
        print('-----------------')
        continue
