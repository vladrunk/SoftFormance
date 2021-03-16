from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        start()


def start():
    # Получаем от юзера форматы данных
    data_formats = __get_data_formats()
    for (data_count_list, data_len_list) in data_formats:
        # Пустой список списков требуемой длины
        data = [[] for _ in range(data_count_list)]
        # Заполянем последовательными числами от 1
        __fill_data(data, data_count_list, data_len_list)
        # Вывод результата на экран
        print(data)


def __fill_data(data: list, count_list: int, len_list: int):
    """
    Заполняем данныыми входящий список
    :param data: список состоящий из "count_list" списков
    :param count_list: кол-во списков в списке "data"
    :param len_list: кол-во элементов в одном списке внутри "data"
    """
    # Предельное значение последовательности
    limit = count_list * len_list
    # Текущий список, значение добавляемое в последовательность
    cur_pos, num = 0, 1
    # Пока не превысили предел
    while num <= limit:
        # Добавляем в конец значение
        data[cur_pos].append(num)
        # Если остаток от деление значения на длину списка в списке равен 0
        if not num % len_list:
            # Переходим в следующий список
            cur_pos += 1
        num += 1


def __get_data_formats() -> list:
    """
    Ввод параметров форматирования списков, валидация ввода
    :return: list
    """
    # Вводы юзера, счетчик итератора
    user_inputs_list, i = [], 1
    while i < 5:
        # Запрос ввода юзера, разбивка его по запятую и
        # добавление если елемент ввода целое число и больше 0
        user_input = [
            int(d) for d in input(f'Enter #{i}: ').split(',')
            if d.isdecimal() and int(d) > 0
        ]
        # Если длина ввода не равна 2
        if len(user_input) != 2:
            print(f'Wrong input #{i}. Try again...')
            #  Повтор ввода
            continue
        else:
            # Инк-т счетчика
            i += 1
            # Добаление ввода в общий список
            user_inputs_list.append(user_input)
    return user_inputs_list
