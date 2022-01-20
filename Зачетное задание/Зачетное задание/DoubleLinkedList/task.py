from abc import abstractmethod
from typing import Iterable, Optional, Any, _T, overload

from collections.abc import MutableSequence

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None

        self.list_nodes = None
        if data is not None:
            self.init_linked_list(data)

    def _step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:  # для for
            raise IndexError()
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self._step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> Any:
        node = self._step_by_step_on_nodes(index)
        node.value = value
        return node.value






    def init_linked_list(self, data: Iterable):
        """ Метод, который создает вспомогательный список и связывает в нём узлы."""
        self.list_nodes = [Node(value) for value in data]
        self.head = self.list_nodes[0]
        self.len = len(self.list_nodes)

        for i in range(len(self.list_nodes) - 1):
            current_node = self.list_nodes[i]
            next_node = self.list_nodes[i + 1]
            self.linked_nodes(current_node, next_node)

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)





    def __str__(self) -> str:
        return f"{[node for node in self]}"

    def __len__(self):
        return self.len

    def index(self, value: Any) -> int:
        """Метод возвращает индекс узла по указанному значению"""
        i = 0
        while i < self.len:
            node = self.step_by_step_on_nodes(i)
            if node.value == value:
                break
            else:
                i += 1
        if i == self.len:
            raise ValueError
        return i

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def count(self, sub: Any) -> int:
        """Метод возвращает количество вхождений указанного значения в список"""
        i = 0
        sum = 0
        while i < self.len:
            node = self.step_by_step_on_nodes(i)
            if node.value == sub:
                i += 1
                sum += 1
            else:
                i += 1
        return sum

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self.len += 1

    def extend(self, value: list) -> None:
        """ Добавление всех элементов списка в конец связного списка. """
        for i in range(len(value)):
            self.append(value[i])

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.__next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index-1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index-1)
            del_node = prev_node.next
            next_node = del_node.__next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def pop(self, index: int) -> Node:
        """ удаляет элемент из списка и возвращает элемент """
        node = self.step_by_step_on_nodes(index)
        a = node.value
        self.__delitem__(index)
        return a

    # auto
    def insert(self, index: int, value: _T) -> None:
        pass

    @overload
    @abstractmethod
    def __setitem__(self, i: int, o: _T) -> None: ...

    @overload
    @abstractmethod
    def __setitem__(self, s: slice, o: Iterable[_T]) -> None: ...

    def __setitem__(self, i: int, o: _T) -> None:
        pass


class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":
    ...
