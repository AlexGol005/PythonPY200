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

    def step_by_step_on_nodes(self, index: int) -> Node:
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
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> Any:
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        if self._len > 2:
            if index == self._len - 1:
                left_node = self.step_by_step_on_nodes(index - 1)
                left_node.next = None

            elif index == 0:
                self._head = self.step_by_step_on_nodes(index + 1)
                self._len -= 1
            else:
                left_node = self.step_by_step_on_nodes(index - 1)
                right_node = self.step_by_step_on_nodes(index + 1)
                left_node.next = right_node
                self._len -= 1
        elif 1 < self._len <= 2:
            if index == 1:
                self.head = self.step_by_step_on_nodes(index - 1)
                self._len -= 1
            elif index == 0:
                self.head = self.step_by_step_on_nodes(index + 1)
                self._len -= 1
        else:
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
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self._linked_nodes(prev_node, insert_node)
            self._linked_nodes(insert_node, next_node)
            self._len += 1

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)
        if self._len == 0:
            self._head = append_node
        else:
            last_index = self._len - 1
            last_node = self.step_by_step_on_nodes(last_index)
            self._linked_nodes(last_node, append_node)
        self._len += 1

    def index(self, value: Any, start: int = 0, stop: int = None) -> int:
        """Метод возвращает индекс узла по указанному значению"""
        if stop is None:
            stop = len(self)
        while start < stop:
            node = self.step_by_step_on_nodes(start)
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
            node = self.step_by_step_on_nodes(i)
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
        node = self.step_by_step_on_nodes(index)
        self.__delitem__(index)
        return node.value

class DoubleLinkedList(LinkedList):

    @staticmethod
    def linked_nodes(left_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None) -> None:
        """
        Функция, которая связывает между собой два узла.
        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node._next = right_node
        right_node._prev = left_node

    def step_by_step_on_nodes(self, index: int) -> Any:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self._len:  # для for
            raise IndexError()
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def _init_linked_list(self, data: Iterable):
        """ Метод, который создает вспомогательный список и связывает в нём узлы. """
        self.list_nodes = [DoubleLinkedNode(value) for value in data]
        self._head = self.list_nodes[0]
        self._len = len(self.list_nodes)
        for i in range(len(self.list_nodes) - 1):
            current_node = self.list_nodes[i]
            next_node = self.list_nodes[i + 1]
            self._linked_nodes(current_node, next_node)

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """
        append_dnode = DoubleLinkedNode(value)
        if self._head is None:
            self._head = append_dnode
        else:
            last_index = self._len - 1
            last_dnode = self.step_by_step_on_nodes(last_index)
            self._linked_nodes(last_dnode, append_dnode)
        self._len += 1

    def insert(self, index: int, value: Any) -> None:  # todo здесь и везде - проверки типов
        insert_node = DoubleLinkedNode(value)
        if index == 0:
            insert_node.next = self._head
            self._head = insert_node
            self._linked_nodes(self._head, insert_node.next)
            self._len += 1
        elif index >= self._len:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            self._linked_nodes(prev_node, insert_node)
            self._linked_nodes(insert_node, next_node)
            self._len += 1

    def index(self, value: Any, start: int = 0, stop: int = None) -> int:
        """Метод возвращает индекс узла по указанному значению"""
        if stop is None:
            stop = len(self)
        while start < stop:
            node = self.step_by_step_on_nodes(start)
            if node.value == value:
                break
            else:
                start += 1
        if start == self._len:
            raise ValueError
        return start

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def count(self, sub: Any) -> int:
        """Метод возвращает количество вхождений указанного значения в список"""
        i = 0
        sum_ = 0
        while i < self._len:
            node = self.step_by_step_on_nodes(i)
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
        node = self.step_by_step_on_nodes(index)
        self.__delitem__(index)
        return node.value


if __name__ == "__main__":
    print('создаём односвязный и двусвязный список и печатаем их:')
    list_ = ['a', 'b', 'c']
    ll = LinkedList(list_)
    dll = DoubleLinkedList(list_)
    print(ll)
    print(dll)
    print('к односвязному и двусвязному списку применяем append и печатаем:')
    ll.append(5)
    dll.append(5)
    ll.append('t')
    dll.append('t')
    print(ll)
    print(dll)
    print('в односвязном и двусвязном списке c append проверяем как связаны узлы:')
    print(ll.list_nodes)
    print(dll.list_nodes)
    print('к односвязному и двусвязному списку применяем insert и печатаем:')
    ll.insert(1, 9)
    dll.insert(1, 9)
    print(ll)
    print(dll)
    print('в односвязном и двусвязном списке c append проверяем как связаны узлы и листнодес это не показывает:')
    print(ll.list_nodes)
    print(dll.list_nodes)
    print('степ бай степ если у ноды убрать репр и стр:')
    for i in range(len(ll) - 1):
        print(ll.step_by_step_on_nodes(i))
    for i in range(len(dll) - 1):
        print(dll.step_by_step_on_nodes(i))
