import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)

if __name__ == '__main__':
    # Генератор нужно обернуть в list(), чтобы увидеть все числа сразу
    result = list(gen_random(5, 1, 3))
    print("Результат:", result)