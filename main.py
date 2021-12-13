def create_dict(file):

    def dict_unit():
        ingridient = []
        recept_dict = {}
        for line in range(int(file.readline())):
            ingridient.append(file.readline().split('|'))
            recept_dict['ingredient_name'] = ingridient[line][0]
            recept_dict['quantity'] = ingridient[line][1]
            recept_dict['measure'] = ingridient[line][2].strip('\n')
            ingridient_dic.append(recept_dict)
        file.readline()
        return ingridient_dic

    cook_book = {}
    with open(file, 'r', encoding='UTF-8') as file:
        for line in file:
            name_eat = line
            ingridient_dic = []
            cook_book[name_eat.strip('\n')] = dict_unit()
    return cook_book

file = 'recipes.txt'
print(create_dict(file))