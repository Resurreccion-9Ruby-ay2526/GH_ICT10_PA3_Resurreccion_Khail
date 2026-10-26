# Working With Dictionaries
from pyscript import display, document


def game_details(e):
    document.getElementById('result').innerHTML = ''
    favorite_game = document.getElementById('dictionary').value

    game_developers = {
        'roblox':'David Baszucki',
        'codm':'TiMi Studio',
        'fnaf':'Scott Cawthon',
        'minecraft':'Notch'
        # specifying dictionaries
    }

    game_check = favorite_game in game_developers

    display_message = ('Sorry, your game is not in the list', f'{game_developers}')
    display(display_message[game_check], target="result")

    game_developers['genshin impact'] = 'Hoyoverse' # adding a new elemetn
    display(game_developers, target='result')


    list_with_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
    tuple_with_strings = ('ab', 'cd', 'ef')
    list_with_strings = ['ax', 'by', 'cz']

    display(dict(list_with_tuples), target='result')
    display(dict(tuple_with_strings), target='result')
    display(dict(list_with_strings), target='result')

    keywords = ['say','jm','jay','mace']
    values =['esguerra', 'piansay', 'estrada', 'panela']

    students_nicknames = dict(zip(keywords, values)) # combining after conversion

    display(students_nicknames, target='result')
    vantage = {
        'c':'Yves ong',
        'pf':'Maiko ebora',
        'sf':'Jaden o',
        'sg':'Seth ngo',
        'pg':'Manu de jesus'
    }

    vantage['pg'] = 'Emman Dylim' #updating
    del vantage['sg']
    display(vantage, target='result')

    dict1 = {'x':1, 'y':2, 'z':3}
    dict2 = {'a':4, 'b':5, 'c':6}

    display(dict1 | dict2, target='result') # combining
    merged_dictionary = {**dict1, **dict2}

    display(merged_dictionary, target='result')

    display(len(merged_dictionary), target='result') # counting

    ai = {
        'tony stark':'creator',
        'JARVIS':'AI1',
        'FRIDAY':'AI2',
        'ULTRON':'AI3',
        'VERONICA':'AI4'
    }

    display('VERONICA' in ai, target='result') # checking
    display(ai.get('JARVIS'), target='result') # getting the value
    display(ai.keys(), target='result') # getting all the keywords
    display(ai.values(), target='result') # getting all the values
    display(ai['tony stark'], target='result')



