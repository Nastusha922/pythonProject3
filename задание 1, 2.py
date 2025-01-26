cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:
    while True:
        dish_name = f.readline().strip()
        if not dish_name:  # Если строка пустая, выходим из цикла
            break

        ingredients_num = int(f.readline().strip())  # Читаем количество ингредиентов

        ingredients_list = []  # Список для хранения ингредиентов
        for _ in range(ingredients_num):
            line = f.readline().strip()
            if not line:  # Пропускаем пустые строки, если они есть
                continue

            name, quantity, measure = line.split('|')  # Разделяем строку на компоненты
            ingredient_dict = {
                'ingredient_name': name.strip(),
                'quantity': quantity.strip(),
                'measure': measure.strip()
            }
            ingredients_list.append(ingredient_dict)  # Добавляем ингредиент в список

        f.readline()
        cook_book[dish_name] = ingredients_list  # Добавляем блюдо и его ингредиенты в словарь

#print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}

    for dish_name in dishes:
        recipe = cook_book.get(dish_name)

        if recipe:
            for ing in recipe:
                name = ing['ingredient_name']
                measure = ing['measure']
                amount = int(ing['quantity']) * person_count

                if name not in ingredients:
                    ingredients[name] = {
                        'measure': measure,
                        'quantity': amount
                    }
                else:
                    ingredients[name]['quantity'] += amount

    return ingredients

ingredients = get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 3)

print(ingredients)




