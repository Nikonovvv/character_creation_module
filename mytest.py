# # Тестовые данные.
# TEST_DATA: list[tuple[int, str, bool]] = [
#     (44, 'success', True),
#     (16, 'failure', True),
#     (4, 'success', False),
#     (21, 'failure', False),
# ]

# BONUS: float = 1.1
# ANTIBONUS: float = 0.8


# def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
#     current_rep += rep_points
#     if buf_effect:
#         return current_rep * BONUS
#     return current_rep


# def remove_rep(current_rep: float, rep_points: int, debuf_effect:
#                bool) -> float:
#     current_rep -= rep_points
#     if debuf_effect:
#         return current_rep * ANTIBONUS
#     return current_rep


# def main(duel_res: list[tuple[int, str, bool]]) -> str:
#     current_rep: float = 0.0
#     for rep, result, effect in duel_res:
#         if result == 'success':
#             current_rep = add_rep(current_rep, rep, effect)
#         if result == 'failure':
#             current_rep = remove_rep(current_rep, rep, effect)
#     return (f'После {len(duel_res)} поединков, репутация персонажа '
#             f'— {current_rep:.3f} очков.')


# # Тестовый вызов функции main.
# print(main(TEST_DATA))

# poi = None
# print (type(poi))



#import math

# Спросим, что хорошего в этой библиотеке.
# print(__doc__)


# message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
#           'квадратного корня из заданного числа'


# def CalculateSquareRoot(Number):
#     """ Вычисляет квадратный корень"""
#     return CalculateSquareRoot(Number)




# def calc(your_number):
#     if your_number <= 0:
#         return

#     print(f'Мы вычислили квадратный корень из введённого вами числа. '
#           f'Это будет: {CalculateSquareRoot(your_number)}')


# print(message)
# calc(25.5)


def avg(first_num, second_num):
    return first_num + second_num / 2

print(avg(5, 10)) 
print(avg(5, 10)) 


