import json
import sys
import time
from random import randint

# Декоратор для вывода результата
def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

# Контекстный менеджер для замера времени
class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"time: {time.time() - self.start:.5f}")

path = sys.argv[1] if len(sys.argv) > 1 else 'data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    # Сортировка без учета регистра, множество для удаления дублей
    return sorted(list(set(item['job-name'] for item in arg)), key=lambda x: x.lower())

@print_result
def f2(arg):
    # Фильтрация по началу строки (без учета регистра для надежности)
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    # Добавление текста к каждой профессии
    return list(map(lambda x: x + ' с опытом Python', arg))

@print_result
def f4(arg):
    # Генерация зарплат и объединение с названиями
    salaries = [randint(100000, 200000) for _ in range(len(arg))]
    return list(zip(arg, salaries))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))