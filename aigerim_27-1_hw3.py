word = input('Введите слово: ').lower()
vowels = 'аеёиоуэюяыaeiou'
consonants = 'бвгджзйклмнпрстфхцчшщьъbcdfghjklmnpqrstvwxyz'
vowels_count = 0
consonants_count = 0

for letter in word:
    if letter in vowels:
        vowels_count += 1
    if letter in consonants:
        consonants_count += 1
print(f'Слово: {word}')
print(f'Количество букв: {len(word)}')
print(f'Согласных букв: {consonants_count}')
print(f'Гласных букв: {vowels_count}')
print('Гласные|Согласные:', round(vowels_count / len(word) * 100, 2), '%', '/',
      round(consonants_count / len(word) * 100, 2), '%')
