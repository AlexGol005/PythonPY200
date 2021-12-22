from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_
        ...  # TODO добавить атрибуты

    def get_value(self) -> Any:
        """Метод, который возвращает значение атрибута value"""
        return self.value

    def get_next(self) -> Optional['Node']:
        return self.next
        # TODO вернуть значение узла

    # TODO добавить метод get_next


if __name__ == '__main__':
    first_node = Node(1)  # первый узел
    second_node = Node(2)  # второй узел

    print(first_node.get_value())
    print(first_node.get_next())

    # TODO с помощью метода распечатать значение первого узла
    # TODO  с помощью метода распечатать следующий узел второго узла

    first_node = Node(1)  # первый узел
    second_node = Node(2)  # второй узел
    first_node.next = second_node
    ''
    first_node = Node(1, second_node)