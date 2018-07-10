my_dict = { 'name': 'Jose', 'age': 90, 'grades': [14, 43, 66, 90] }

another_dict = { 1: 15, 2: 64, 3: 124}

lottery_players = [
{
    'name': 'Rolf',
    'numbers': (12, 34, 54, 675, 34)
},
{
    'name': 'Bill',
    'numbers': (15, 117, 44, 64, 90)
}
]

universities = [
{
    'name': 'Oxford',
    'location': 'UK'
},
{
    'name': 'MIT',
    'location': 'US'
}
]

sum(lottery_player['numbers'])

lottery_player['name'] = 'John' # updates name

# lottery_player['numbers'][0] = 50 # can't modify a tuple