def divisors_list(x: int) -> list:
    """
    Вычисляет уникальные делители числа

    ARGS:
        x (int): число

    RETURNS:
        list: список делителей
    """

    # MEANS: список делителей
    d_list: list

    # создание списка делителей перебором до корня
    d_list = [i for i in range(1, int(x ** 0.5) + 1) if x % i == 0]

    # добавляем делители x // i (кроме случая, когда i равно x // i) в обратном порядке
    d_list += [x // i for i in reversed(d_list) if i != x // i]

    # возвращаем этот список отсортированным
    return sorted(d_list)
