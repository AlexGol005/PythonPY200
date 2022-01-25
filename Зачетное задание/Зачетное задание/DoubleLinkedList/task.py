from abc import abstractmethod
from typing import Iterable, Optional, Any

from collections.abc import MutableSequence

from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self._len = 0
        self._head: Optional[Node] = None
        self._list_nodes = None
        if data is not None:
            self._init_linked_list(data)

    def _init_linked_list(self, data: Iterable):
        """ Метод, который создает вспомогательный список и связывает в нём узлы. """
        self.list_nodes = [Node(value) for value in data]
        self._head = self.list_nodes[0]
        self._len = len(self.list_nodes)
        for i in range(len(self.list_nodes) - 1):
            current_node = self.list_nodes[i]
            next_node = self.list_nodes[i + 1]
            self._linked_nodes(current_node, next_node)

    def _step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self._len:  # для for
            raise IndexError()
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    @staticmethod
    def _linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self._step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> Any:
        node = self._step_by_step_on_nodes(index)
        node.value = value


    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self._len:
            raise IndexError()
        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            tail = self._step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next
            self._linked_nodes(prev_node, next_node)
        self._len -= 1

    def __len__(self):
        return self._len

    def __str__(self) -> str:
        return f"{[node for node in self]}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({[node for node in self]})"

    def insert(self, index: int, value: Any) -> None:  # todo здесь и везде - проверки типов
        insert_node = Node(value)
        if index == 0:
            insert_node.next = self._head
            self._head = insert_node
            self._linked_nodes(self._head, insert_node.next)
            self._len += 1
        elif index >= self._len:
            self.append(value)
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self._linked_nodes(prev_node, insert_node)
            self._linked_nodes(insert_node, next_node)
            self._len += 1

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)
        if self._head is None:
            self._head = append_node
        else:
            last_index = self._len - 1
            last_node = self._step_by_step_on_nodes(last_index)

            self._linked_nodes(last_node, append_node)

        self._len += 1

    def index(self, value: Any, start: int = 0, stop: int = None) -> int:
        """Метод возвращает индекс узла по указанному значению"""
        if stop is None:
            stop = len(self)
        while start < stop:
            node = self._step_by_step_on_nodes(start)
            if node.value == value:
                break
            else:
                start += 1
        if start == self._len:
            raise ValueError
        return start

    # def to_list(self) -> list:
    #     return [linked_list_value for linked_list_value in self]

    def count(self, sub: Any) -> int:
        """Метод возвращает количество вхождений указанного значения в список"""
        i = 0
        sum_ = 0
        while i < self._len:
            node = self._step_by_step_on_nodes(i)
            if node.value == sub:
                i += 1
                sum_ += 1
            else:
                i += 1
        return sum_

    def extend(self, value: list) -> None:
        """ Добавление всех элементов списка в конец связного списка. """
        for i in range(len(value)):
            self.append(value[i])

    def pop(self, index: int = None) -> Any:
        """ удаляет элемент из списка и возвращает элемент """
        if index is None:
            index = len(self)
        node = self._step_by_step_on_nodes(index)
        self.__delitem__(index)
        return node.value


class DoubleLinkedList(LinkedList):

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self._len:
            raise IndexError()
        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            tail = self._step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next
            self._linked_nodes(prev_node, next_node)
        self._len -= 1

    def __len__(self):
        return self._len

    def __str__(self) -> str:
        return f"{[node for node in self]}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({[node for node in self]})"

    def insert(self, index: int, value: Any) -> None:  # todo здесь и везде - проверки типов
        insert_node = Node(value)
        if index == 0:
            insert_node.next = self._head
            self._head = insert_node
            self._linked_nodes(self._head, insert_node.next)
            self._len += 1
        elif index >= self._len:
            self.append(value)
        else:
            prev_node = self._step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self._linked_nodes(prev_node, insert_node)
            self._linked_nodes(insert_node, next_node)
            self._len += 1

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)
        if self._head is None:
            self._head = append_node
        else:
            last_index = self._len - 1
            last_node = self._step_by_step_on_nodes(last_index)

            self._linked_nodes(last_node, append_node)

        self._len += 1

    def index(self, value: Any, start: int = 0, stop: int = None) -> int:
        """Метод возвращает индекс узла по указанному значению"""
        if stop is None:
            stop = len(self)
        while start < stop:
            node = self._step_by_step_on_nodes(start)
            if node.value == value:
                break
            else:
                start += 1
        if start == self._len:
            raise ValueError
        return start

    # def to_list(self) -> list:
    #     return [linked_list_value for linked_list_value in self]

    def count(self, sub: Any) -> int:
        """Метод возвращает количество вхождений указанного значения в список"""
        i = 0
        sum_ = 0
        while i < self._len:
            node = self._step_by_step_on_nodes(i)
            if node.value == sub:
                i += 1
                sum_ += 1
            else:
                i += 1
        return sum_

    def extend(self, value: list) -> None:
        """ Добавление всех элементов списка в конец связного списка. """
        for i in range(len(value)):
            self.append(value[i])

    def pop(self, index: int = None) -> Any:
        """ удаляет элемент из списка и возвращает элемент """
        if index is None:
            index = len(self)
        node = self._step_by_step_on_nodes(index)
        self.__delitem__(index)
        return node.value


if __name__ == "__main__":
    # проверка методов для односвязного списка
    list_ = ['a', 'b', 'c']
    ll = LinkedList(list_)
    print(ll[1])  # ll.__getitem__(1)
    print(ll.__setitem__(1, 'v'))  # Expected: ['a', 'v', 'c']
    print(ll)
    ll.__delitem__(1)
    print(ll)
    ll.insert(3, 'b')
    print(ll)
    print(len(ll))
    ll.append('d')
    print(ll)
    print(ll.index('b'))
    print(ll.count('b'))
    ll.extend(['df', 'as'])
    print(ll)
    print(ll.pop(4))
    print(ll)
    print('-'*50)
    print(DoubleLinkedList(list_))
    dll = DoubleLinkedList(list_)
    print(dll[1])
    dll[1] = 1
    print(dll)


str_1 = "test"
str_2 = "test"

str_1 == str_2  # True
str_1 is str_2  # False