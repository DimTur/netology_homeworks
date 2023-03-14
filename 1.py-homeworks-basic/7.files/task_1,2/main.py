from pprint import pprint

file_name = 'Recepts.txt'


def recepts_reader():
    with open(file_name, encoding = 'utf-8') as recepts_obj:
        cook_book = {}
        for line in recepts_obj:
            dishes_name = line.strip()
            cook_book.update({dishes_name: []})
            for ingr in range(int(recepts_obj.readline())):
                ingredient = recepts_obj.readline().strip().split(' | ')
                dict_ingredients = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                cook_book[dishes_name].append(dict_ingredients)
            recepts_obj.readline()
    return cook_book


# book = recepts_reader(file_name)
# pprint(book)

def get_shop_list_by_dishes(dishes, person_count):
    ingridient_list = {}
    for ingred in dishes:
        for ingr in recepts_reader()[ingred]:
            name_ingr = ingr.pop('ingredient_name')
            ingr['quantity'] = int(ingr['quantity']) * int(person_count)
            if name_ingr in ingridient_list:
                ingr['quantity'] += ingridient_list[name_ingr]['quantity']
            ingridient_list.update({name_ingr: ingr})
    return ingridient_list

dinner = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(dinner)