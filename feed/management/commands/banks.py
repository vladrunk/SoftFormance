from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        start()


def start():
    # Получаем список паролей
    passwords = __get_data()
    allowed_passwords = []
    # Проход по каждому паролю
    for password in passwords:
        # Если каждая функция-проверка возвращает True
        if all([__checkLetter(password), __checkInt(password), __checkCap(password),
                __consistSpecsChars(password), __checkLen(password), not __hasSpace(password)]):
            # добавляем пароль в список допустимых
            allowed_passwords.append(password)
    # Печать всех допустимых паролей
    print(','.join(allowed_passwords))


def __get_data() -> list:
    """
    Ввод списка паролей разделённых запятыми.
    :return: list
    """
    return input('Enter passwords, separate by comma: ').split(',')


def __checkCap(string: str) -> bool:
    """
    Проверка строки на хотя бы один заглавный символ
    :param string: проверяемая строка
    :return: bool
    """
    return __checkFunc(string, str.isupper)


def __checkLetter(string: str) -> bool:
    """
    Проверка строки на хотя бы один строчный символ
    :param string: проверяемая строка
    :return: bool
    """
    return __checkFunc(string, str.islower)


def __checkInt(string: str) -> bool:
    """
    Проверка строки на хотя бы один цифровой символ
    :param string: проверяемая строка
    :return: bool
    """
    return __checkFunc(string, str.isdigit)


def __checkFunc(string: str, func) -> bool:
    """
    Проверка строки функцией
    :param string: проверяемая строка
    :param func: функция проверки
    :return: bool
    """
    # Проходимя по каждому символу
    for s in string:
        # и проверка символа функцией
        if func(s):
            return True
        else:
            continue
    return False


def __consistSpecsChars(string: str) -> bool:
    """
    Проверка строки на содержания хотя бы одного символа *#+@
    :param string: проверяемая строка
    :return: bool
    """
    for s in string:
        if s in '*#+@':
            return True
        else:
            continue
    return False


def __checkLen(string: str) -> bool:
    """
    Проверка длины строки. Не менее 4, не более 5 символов.
    :param string: проверяемая строка
    :return: bool
    """
    return 4 <= len(string) <= 6


def __hasSpace(string: str) -> bool:
    """
    Проверка строки на наличие пробельного символа.
    :param string: проверяемая строка
    :return: bool
    """
    # Считаем кол-во пробелов и преобразуем рез-ат в тип bool
    return bool(string.count(' '))
