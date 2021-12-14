def create_dict(file):

    def dict_unit():
        ingridient_dic = []
        for line in range(int(file.readline())):
            recept_dict = {}
            ingridient = (file.readline().split('|'))
            recept_dict['ingredient_name'] = ingridient[0]
            recept_dict['quantity'] = int(ingridient[1].strip())
            recept_dict['measure'] = ingridient[2].strip('\n')
            ingridient_dic.append(recept_dict)
        return ingridient_dic

    cook_book = {}
    with open(file, 'r', encoding='UTF-8') as file:
        while True:
            name_eat = file.readline()
            if not name_eat:
                break
            cook_book[name_eat.strip('\n')] = dict_unit()
            file.readline()
    return cook_book

file = 'recipes.txt'
print(create_dict(file))