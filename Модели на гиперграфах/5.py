import numpy as np
import time
from scipy.optimize import linprog

def simplex_min(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None):
    c = np.array(c)
    if A_ub is not None:
        A_ub = np.array(A_ub)
    if b_ub is not None:
        b_ub = np.array(b_ub)
    if A_eq is not None:
        A_eq = np.array(A_eq)
    if b_eq is not None:
        b_eq = np.array(b_eq)

    num_vars = len(c)
    num_constraints = 0
    if A_ub is not None:
        num_constraints += A_ub.shape[0]
    if A_eq is not None:
        num_constraints += A_eq.shape[0]

    # Создаем начальную таблицу симплекс-метода
    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
    tableau[0, :num_vars] = c
    tableau[0, -1] = 0

    if A_ub is not None:
        tableau[1:num_constraints + 1, :num_vars] = A_ub
        tableau[1:num_constraints + 1, -1] = b_ub
        tableau[1:num_constraints + 1, num_vars:num_vars + num_constraints] = np.eye(num_constraints)

    iteration = 0
    while True:
        entering = np.argmin(tableau[0, :-1])
        if tableau[0, entering] >= 0:
            break

        ratios = np.full((num_constraints,), np.inf)
        for i in range(num_constraints):
            if tableau[i + 1, entering] > 0:
                ratios[i] = tableau[i + 1, -1] / tableau[i + 1, entering]

        leaving = np.argmin(ratios) + 1

        pivot = tableau[leaving, entering]
        tableau[leaving, :] /= pivot
        for i in range(tableau.shape[0]):
            if i != leaving:
                tableau[i, :] -= tableau[i, entering] * tableau[leaving, :]

        iteration += 1

    # Извлечение результатов
    x = np.zeros(num_vars)
    for i in range(1, num_constraints + 1):
        if np.sum(tableau[i, :num_vars] == 1) == 1 and np.sum(tableau[i, :num_vars] == 0) == num_vars - 1:
            x[np.argmax(tableau[i, :num_vars])] = tableau[i, -1]


    return {
        'x': x,
        'fun': -tableau[0, -1],  # Изменяем знак, так как мы минимизируем
        'success': True,
        'status': 0,
        'message': 'Optimization terminated successfully.'
    }

def simplex_max(c, A_ub=None, b_ub=None):
    c = np.array(c)
    if A_ub is not None:
        A_ub = np.array(A_ub)
    if b_ub is not None:
        b_ub = np.array(b_ub)

    num_vars = len(c)
    num_constraints = A_ub.shape[0] if A_ub is not None else 0

    # Создаем начальную таблицу симплекс-метода
    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
    tableau[0, :num_vars] = c
    tableau[0, -1] = 0

    # Заполнение таблицы для ограничений
    if A_ub is not None:
        tableau[1:num_constraints + 1, :num_vars] = A_ub
        tableau[1:num_constraints + 1, -1] = b_ub
        # Добавляем слабые переменные
        tableau[1:num_constraints + 1, num_vars:num_vars + num_constraints] = np.eye(num_constraints)

    # Основной цикл симплекс-метода
    iteration = 0
    while True:

        # Находим столбец с наибольшим значением
        entering = np.argmax(tableau[0, :-1])
        if tableau[0, entering] <= 0:
            break

        # Находим строку с наименьшим положительным соотношением
        ratios = np.full((num_constraints,), np.inf)
        for i in range(num_constraints):
            if tableau[i + 1, entering] > 0:  # Проверяем только положительные значения
                ratios[i] = tableau[i + 1, -1] / tableau[i + 1, entering]
            else:
                ratios[i] = np.inf  # Если не положительное, задаем бесконечность

        # Проверка на случай, если все значения в ratios равны бесконечности
        if np.all(ratios == np.inf):
            print("Ошибка: нет положительной выходной переменной. Останов.")
            break

        leaving = np.argmin(ratios) + 1

        # Обновляем таблицу
        pivot = tableau[leaving, entering]
        tableau[leaving, :] /= pivot  # Нормализуем строку выходной переменной
        for i in range(tableau.shape[0]):
            if i != leaving:
                tableau[i, :] -= tableau[i, entering] * tableau[leaving, :]

        iteration += 1

    # Извлечение результатов
    x = np.zeros(num_vars)
    for i in range(1, num_constraints + 1):
        if np.sum(tableau[i, :num_vars] == 1) == 1 and np.sum(tableau[i, :num_vars] == 0) == num_vars - 1:
            x[np.argmax(tableau[i, :num_vars])] = tableau[i, -1]


    return {
        'x': x,
        'fun': tableau[0, -1],  # Мы максимизируем, поэтому берем значение без изменения
        'success': True,
        'status': 0,
        'message': 'Optimization terminated successfully.'
    }



# Функция для тестирования задач
def run_test(c, A_ub, b_ub):
    print("\nТестовая задача:")
    print("Целевая функция:", c)
    print("Ограничения A_ub:", A_ub)
    print("Ограничения b_ub:", b_ub)

    # Запуск вашей реализации
    start_time = time.time()
    #my_result = simplex_min(c, A_ub=A_ub, b_ub=b_ub)
    my_result = simplex_max(c, A_ub=A_ub, b_ub=b_ub)
    my_time = time.time() - start_time

    # Запуск функции scipy
    start_time = time.time()
    scipy_result = linprog(c, A_ub=A_ub, b_ub=b_ub, method='simplex')
    scipy_time = time.time() - start_time

    # Печать результатов
    print("\nРезультаты нашей реализации:")
    print("x:", my_result['x'])
    print("fun:", my_result['fun'])
    print("success:", my_result['success'])
    print("Время выполнения нашей реализации:", my_time)

    print("\nРезультаты функции scipy:")
    print("x:", scipy_result.x)
    print("fun:", scipy_result.fun)
    print("success:", scipy_result.success)
    print("Время выполнения функции scipy:", scipy_time)
    print("\n------------------------------\n")


tests = [
    ([1, 1], [[1, 0], [0, 1]], [4, 6]),
    ([2, 3], [[1, 2], [1, 1], [2, 1]], [8, 6, 10]),
    ([3, 2], [[1, 1], [0, 1]], [5, 3]),
    ([0, 1], [[1, 1], [2, 1]], [6, 8]),
    ([1, 2], [[2, 1], [1, 2]], [8, 6])
]

# tests = [
#     ([-1, -2], [[2, 1], [1, 1], [1, 0]], [20, 16, 8]),
#     ([3, 2], [[-2, -1], [-1, 0]], [-10, -5]),
#     ([-2, -1], [[-1, -2], [1, 1], [0, 1]], [-4, 10, 6]),
#     ([1, 3], [[2, 1], [1, 1], [1, 0]], [20, 16, 8]),
#     ([1, 2], [[1, 1], [-1, 2], [-2, -1]], [15, 10, 5])
# ]

for c, A_ub, b_ub in tests:
    run_test(c, A_ub, b_ub)