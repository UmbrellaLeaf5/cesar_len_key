# Моя небольшая библиотека :)

def divisors_list(x: int) -> list[int]:
    """
    Does:
        вычисляет уникальные делители числа

    Args:
        x (int): число

    Returns:
        list: список делителей
    """

    ic()

    # Means: список делителей
    d_list: list[int]

    # создание списка делителей перебором до корня
    d_list = [i for i in range(1, int(x ** 0.5) + 1) if x % i == 0]

    # добавляем делители x // i (кроме случая, когда i равно x // i) в обратном порядке
    d_list += [x // i for i in reversed(d_list) if i != x // i]

    # возвращаем этот список отсортированным
    return sorted(d_list)


class switch(object):
    """
    Means:
        специальный класс switch-case
        (использование почти аналогично C++)

    Args:
        object (object): объект, по которому происходит выборка
    """

    def __init__(self, value):
        # значение, которое будем искать
        self.value = value

        # для пустых case блоков
        self.fall = False

    def __iter__(self):
        """
        Does:
            возвращает один раз метод match и завершается
            (нужен для использования в цикле for)

        YIELDS:
            bool: нужно ли заходить в тестовый вариант
        """

        yield self.match
        raise StopIteration

    def match(self, *args) -> bool:
        """
        Does:
            указывает, нужно ли заходить в тестовый вариант

        Returns:
            bool: нужно ли заходить в тестовый вариант
        """

        if self.fall or not args:
            # пустой список аргументов означает последний блок case
            # fall означает, что ранее сработало условие и нужно заходить
            # в каждый case до первого break
            return True

        elif self.value in args:
            self.fall = True
            return True

        return False
