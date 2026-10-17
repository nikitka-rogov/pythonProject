data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    # 1. Без использования lambda (через функцию-ключ)
    def sort_key(x):
        return abs(x)


    result = sorted(data, key=sort_key, reverse=True)
    print(result)

    # 2. С использованием lambda-функции
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)