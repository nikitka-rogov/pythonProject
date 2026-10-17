import json

path = r"C:\Users\user\Downloads\data_light.json"


def f1(data):
    return filter(lambda x: 'программист' in x.get('job-name', '').lower(), data)


def f2(data):
    filtered = filter(lambda x: x.get('salary') is not None and x.get('salary') > 50000, data)
    return map(lambda x: {**x, 'salary': round(x['salary'], -3)}, filtered)


def f3(data):
    def add_python(item):
        item_copy = item.copy()
        if 'key-skills' in item_copy:
            item_copy['key-skills'] = [s + ' с опытом Python' for s in item_copy['key-skills']]
        return item_copy

    return map(add_python, data)


def f4(data):
    return (x['salary'] for x in data if x.get('salary') is not None and 100000 <= x.get('salary') <= 200000)


if __name__ == '__main__':
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = list(f3(f2(f1(data))))

    for item in result[:3]:
        print(item)

    print("\nЗарплаты:")
    for salary in f4(data):
        print(salary)