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

    def __repr__(self) -> str:
        name = self.__class__.__name__
        return f"{name}({self.value}, {None})" if self.next is None else f"{name}({self.value}, {name}({self.next}))"

    # def __str__(self) -> str:
    #     return str(self.value)

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

class DoubleLinkedNode(Node):
    def __init__(self, value, next_=None, prev=None):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self) -> str:
        name = self.__class__.__name__
        return f"{name}({self.value}, {None}, {None}))" if self._next is None and self._prev is None else\
               f"{name}({self.value}, {name}({self._next}), {None})" if self._prev is None else\
               f"{name}({self.value}, {None}, {name}({self._prev}))" if self._next is None else\
               f"{name}({self.value}, {name}({self._next}),{name}({self._prev}))"

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


if __name__ == "__main__":
    dl1 = DoubleLinkedNode(2, DoubleLinkedNode(3), DoubleLinkedNode(1))
    print(repr(dl1))
    print(dl1.prev)
    dnode1 = DoubleLinkedNode(5)
    dnode2 = DoubleLinkedNode(6)
    print(dnode1)
    dnode1.next = DoubleLinkedNode(6)
    dnode1.prev = DoubleLinkedNode(4)
    print(repr(dnode1))
    print(repr(Node(5)))
    print(DoubleLinkedNode(5).value)
    DoubleLinkedNode(5).next = DoubleLinkedNode(6)
    print(repr(DoubleLinkedNode(5)))
    print('----------'*10)
    a = DoubleLinkedNode(1)
    b = DoubleLinkedNode(2)
    c = DoubleLinkedNode(3)
    print(repr(a))
    a.next = b
    print(repr(a))
    b.prev = a
    b.next = c
    print(repr(b))




