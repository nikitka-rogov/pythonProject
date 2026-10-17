from lab_2.rectangle import Rectangle
from lab_2.circle import Circle
from lab_2.square import Square
import colorama  #

# Инициализируем colorama для цветного вывода в консоль
colorama.init()

if __name__ == '__main__':
    N = 10

    # Создаем объекты
    rect = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    # Выводим информацию о фигурах
    print(colorama.Fore.BLUE + str(rect))
    print(colorama.Fore.GREEN + str(circle))
    print(colorama.Fore.RED + str(square))
    print(colorama.Style.RESET_ALL)

    # Демонстрация работы внешнего пакета (в данном случае меняем цвет текста)
    print("Вызов внешнего пакета (colorama) прошел успешно!")