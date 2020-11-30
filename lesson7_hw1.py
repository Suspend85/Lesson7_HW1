import os
from pprint import pprint

FILE_PATH = os.path.join(os.getcwd(), 'recipes.txt')  # Get current workdir


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


print('Кулинарная книга:')
pprint(recipes_parse(FILE_PATH))
