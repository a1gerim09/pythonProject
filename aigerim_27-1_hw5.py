GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
GeekTech.pop('bag')
GeekTech['address'] = 'Ибраимова 103'
GeekTech['telefon'] = 996507052018
GeekTech['insta_acount'] = 'geekteck_edu'
new_courses = ['iOS', 'UX/UI']
GeekTech['courses'] = set(GeekTech['courses'] + new_courses)
GeekTech['founding_date'] = '2018'
courses_count = len(GeekTech['courses'])
for key, value in GeekTech.items():
    print(f'{key}:{value}')
print(f'Количество курсов-{courses_count}')