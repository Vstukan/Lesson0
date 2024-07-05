#Работа со словарями:
my_dict = {'Ivan': 1974, 'Piter': 2003, 'Sasha': 2010}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Piter'])
print('Not existing value:', my_dict.get('John'))
my_dict.update({'Sofia': 1993,
                'Semen': 1986})
print('Deleted value: ', my_dict.get('Piter'))
del my_dict['Piter']
print('Modified dictionary:', my_dict)
#Работа с множествами:
my_set = {45, 'Urban', 45, True, 3.14, 45, True, 3.14, 'Urban'}
print('Set:', my_set)
my_set.update({12, 45, 'Go', (5, 7, 9)})
my_set.discard('Urban')
print('Modified set:', my_set)