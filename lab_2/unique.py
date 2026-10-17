class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.iterator = iter(self.items)

    def __next__(self):
        while True:
            item = next(self.iterator)  # Если элементы закончатся, выбросится StopIteration

            check_item = item.lower() if self.ignore_case and isinstance(item, str) else item

            if check_item not in self.seen:
                self.seen.add(check_item)
                return item  # Возвращаем оригинальное значение

    def __iter__(self):
        return self

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
# Так как это итератор, его тоже лучше превратить в список для вывода
print(list(Unique(data)))

data_str = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
print(list(Unique(data_str, ignore_case=True)))