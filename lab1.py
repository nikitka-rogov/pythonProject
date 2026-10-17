import sys
import math



# 1. ПРОЦЕДУРНАЯ ПАРАДИГМА

def get_coeff_proc(name, index):
    if len(sys.argv) > index:
        try:
            return float(sys.argv[index])
        except ValueError:
            print(f"Ошибка аргумента {name}. Введите вручную.")
    while True:
        try:
            return float(input(f"Введите {name}: "))
        except ValueError:
            print("Ошибка: введите число.")


def solve_procedural():
    print("\n--- Процедурный подход ---")
    a = get_coeff_proc("A", 1)
    b = get_coeff_proc("B", 2)
    c = get_coeff_proc("C", 3)

    d = b ** 2 - 4 * a * c
    roots = []
    if d >= 0:
        t_vals = [-b / (2 * a)] if d == 0 else [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]
        for t in t_vals:
            if t > 0:
                roots.extend([math.sqrt(t), -math.sqrt(t)])
            elif t == 0:
                roots.append(0.0)
    print(f"Корни: {sorted(set(roots)) if roots else 'нет'}")



# 2. ОБЪЕКТНО-ОРИЕНТИРОВАННАЯ ПАРАДИГМА

class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def solve(self):
        d = self.b ** 2 - 4 * self.a * self.c
        roots = []
        if d >= 0:
            t_vals = [-self.b / (2 * self.a)] if d == 0 else [(-self.b + math.sqrt(d)) / (2 * self.a),
                                                              (-self.b - math.sqrt(d)) / (2 * self.a)]
            for t in t_vals:
                if t > 0:
                    roots.extend([math.sqrt(t), -math.sqrt(t)])
                elif t == 0:
                    roots.append(0.0)
        return sorted(set(roots))


def solve_oop():
    print("\n--- ООП подход ---")
    a = get_coeff_proc("A", 1)
    b = get_coeff_proc("B", 2)
    c = get_coeff_proc("C", 3)

    eq = BiquadraticEquation(a, b, c)
    roots = eq.solve()
    print(f"Корни: {roots if roots else 'нет'}")



# 3. ФУНКЦИОНАЛЬНАЯ ПАРАДИГМА

def process_t(t):
    match t:
        case t if t < 0:
            return []
        case 0:
            return [0.0]
        case t if t > 0:
            return [math.sqrt(t), -math.sqrt(t)]


def solve_functional():
    print("\n--- Функциональный подход ---")
    a = get_coeff_proc("A", 1)
    b = get_coeff_proc("B", 2)
    c = get_coeff_proc("C", 3)

    d = b ** 2 - 4 * a * c
    match d:
        case d if d < 0:
            roots = []
        case 0:
            roots = process_t(-b / (2 * a))
        case _:
            sqrt_d = math.sqrt(d)
            roots = process_t((-b + sqrt_d) / (2 * a)) + process_t((-b - sqrt_d) / (2 * a))

    print(f"Корни: {sorted(set(roots)) if roots else 'нет'}")


# ==========================================
# ЗАПУСК
# ==========================================
if __name__ == "__main__":

    solve_procedural()
    solve_oop()
    solve_functional()