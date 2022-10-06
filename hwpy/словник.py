dict_2 = {
    'hello': 'привіт',
    'morning': 'ранок',
    'evening': 'вечір',
    'good': 'добре',
    'friend': 'друг',
    'people': 'люди',
    'work': 'працювати',
    'house': 'будинок',
    'homework': 'домашнє завдання',
    'cave': 'печера',
    'madicine': 'ліки',
    'trip': 'подорож',
    'help': 'допомогти',
    'mountain': 'гора',
    'scale': 'масштаб',
    'can': 'може',
    'cancel': 'скасувати',
    'yes': 'так',
    'no': 'ні',
    'usually': 'зазвичай',
    'tale': 'казка',
}
while True:
    word = input('write a word: ')
    if word in dict_2:
        print(f'{word}- {dict_2[word]}')
    else:
        print(f'\'{word}\' is not in the dict')