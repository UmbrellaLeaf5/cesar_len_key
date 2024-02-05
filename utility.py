def divisors_list(x: int) -> list[int]:
    """
    Вычисляет уникальные делители числа

    ARGS:
        x (int): число

    RETURNS:
        list: список делителей
    """

    # MEANS: список делителей
    d_list: list[int]

    # создание списка делителей перебором до корня
    d_list = [i for i in range(1, int(x ** 0.5) + 1) if x % i == 0]

    # добавляем делители x // i (кроме случая, когда i равно x // i) в обратном порядке
    d_list += [x // i for i in reversed(d_list) if i != x // i]

    # возвращаем этот список отсортированным
    return sorted(d_list)


class switch(object):
    """
    Специальный класс switch-case
    (использование почти аналогично C++)

    пример использования:
    x = int(input())

    for case in switch(x):
        if case(1): pass
        if case(2): pass
        if case(3): 
            print('Число от 1 до 3')
            break
        if case(4): 
            print('Число 4')
        if case(): # default
            print('Другое число')

    ARGS:
        object (_type_): объект, по которому происходит выборка
    """

    def __init__(self, value):
        # значение, которое будем искать
        self.value = value
        # для пустых case блоков
        self.fall = False

    def __iter__(self):
        """
        Возвращает один раз метод match и завершается
        (нужен для использования в цикле for)

        YIELDS:
            bool: нужно ли заходить в тестовый вариант
        """
        yield self.match
        raise StopIteration

    def match(self, *args) -> bool:
        """
        Указывает, нужно ли заходить в тестовый вариант

        RETURNS:
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
