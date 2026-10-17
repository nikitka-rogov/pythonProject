def field(items, *args):
    assert len(args) > 0

    # Если передан только один аргумент
    if len(args) == 1:
        key = args[0]
        for item in items:
            val = item.get(key)
            # Пропускаем, если значения нет или оно равно None
            if val is not None:
                yield val

    # Если передано несколько аргументов
    else:
        for item in items:
            # Создаем новый словарь только с нужными ключами
            new_dict = {k: item[k] for k in args if k in item and item[k] is not None}

            # Выдаем словарь, только если он не пустой (т.е. есть хотя бы одно значение)
            if new_dict:
                yield new_dict
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

# 1. Один аргумент
print(list(field(goods, 'title')))

# 2. Несколько аргументов
print(list(field(goods, 'title', 'price')))
