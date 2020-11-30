# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }

import os
from pprint import pprint


def recipes_parse(filename, encoding='utf-8'):
    res = {}
    with open(filename, encoding=encoding) as recipes:
        line = recipes.readline()
        point = 'recipe_name'
        recipe_name = ''
        while line != '':  # while not EOF
            line = line.strip()
            if point == 'recipe_name':
                point = 'num_of_ingredients'
                recipe_name = line
                res[line] = []
                line = recipes.readline()
                continue
            if point == 'num_of_ingredients':
                point = 'ingredients'
                line = recipes.readline()
                continue
            if point == 'ingredients':
                temp_list = line.split('|')
                if len(temp_list) != 3:  # check for the number of positions in the list
                    point = 'recipe_name'
                    recipe_name = ''
                    line = recipes.readline()
                    continue
                temp_dict = dict(zip(['ingredient_name', 'quantity', 'measure'],
                                    [i.strip() for i in temp_list]))
                res[recipe_name].append(temp_dict)
            line = recipes.readline()
    return res


file_path = os.path.join(os.getcwd(), 'recipes.txt')  # Get current workdir
cook_book = recipes_parse('recipes.txt')
pprint(cook_book)
