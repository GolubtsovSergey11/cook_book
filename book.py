from pprint import pprint

def cool_book():
    with open('cook.txt', encoding='UTF-8') as cook_file:
        my_dict = {}
        for line in cook_file:
            dish_name = line.strip()
            my_dict[dish_name] = []
            counter = int(cook_file.readline().strip())
            for i in range(counter):
                ingredient = cook_file.readline().strip().split('|')
                temp_dict = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                my_dict[dish_name].append(temp_dict)
            cook_file.readline()
        return my_dict

pprint(cool_book())



def get_shop_list_by_dishes():
    cook_dict = cool_book()
    cook_dishes = {}
    while True:
        dishes = input('Введите название блюда: ').capitalize()
        if dishes in cook_dict:
            person = int(input('Введите количество людей: '))
            for ingredient in cook_dict[dishes]:
                cook_dishes[ingredient['ingredient_name']] = {}
                cook_ingredient = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person}
                cook_dishes[ingredient['ingredient_name']] = (cook_ingredient)
            return pprint(cook_dishes)

        else:
            print('''Такого блюда в меню нету.
изучите меню и выберите что Вам нужно:
1) Омлет 
2) Утка по-пекински 
3) Запеченный картофель
4) Фахитос''')

get_shop_list_by_dishes()
