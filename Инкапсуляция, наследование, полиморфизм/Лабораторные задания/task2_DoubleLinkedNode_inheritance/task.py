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
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


# TODO реализовать класс DoubleLinkedNode
class DoubleLinkedNode(Node):
    def __init__(self, prev):
        super().__init__(value=None, next_=None)
        self.prev = prev

    def __repr__(self) -> str:
        name = {self.__class__.__name__}
        return f"{name}({self.value}, {None}, {None})" if self.next_ and self.prev is None else\
               f"{name}({self.value}, {None}, {None})" if self.next_ and self.prev is None else\
               f"{name}({self.value}, {None}, {None})"


    def is_valid(self, dnode: Any) -> None:
        if not isinstance(dnode, (type(None), DoubleLinkedNode)):
            raise TypeError

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"]):
        self.is_valid(prev)
        self._prev = prev
a = DoubleLinkedNode(2, DoubleLinkedNode(3), DoubleLinkedNode(1))