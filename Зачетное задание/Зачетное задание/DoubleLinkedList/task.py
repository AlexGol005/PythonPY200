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

    def _init_linked_list(self, data: Iterable) -> None:
        """ Метод, который создает вспомогательный список и связывает в нём узлы. """
        self.list_nodes = [Node(value) for value in data]
        self._head = self.list_nodes[0]
        self._len = len(self.list_nodes)
        for m in range(len(self.list_nodes) - 1):
            current_node = self.list_nodes[m]
            next_node = self.list_nodes[m + 1]
            self._linked_nodes(current_node, next_node)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError('в step_by_step_on_nodes  не int')
        if not 0 <= index < self._len:  # для for
            raise IndexError('в step_by_step_on_nodes  не тот индекс')
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
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int) -> None:
        """ Метод устанавливает удаляет узел по указанному индексу. """
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

    def __len__(self) -> int:
        """ Метод возвращает длину списка """
        return self._len

    def __str__(self) -> str:
        return f"{[node for node in self]}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({[node for node in self]})"

    def insert(self, index: int, value: Any) -> None:
        """ Метод вставляет узел по указанному индексу"""
        if not isinstance(index, int):
            raise TypeError('в insert  не int')
        if not 0 <= index < self._len:  # для for
            raise IndexError('в insert  не тот индекс')
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
        if start == stop:
            raise ValueError('нету')
        else:
            return start

    def count(self, sub: Any) -> int:
        """Метод возвращает количество вхождений указанного значения в список"""
        counter_ = 0
        sum_ = 0
        while counter_ < self._len:
            node = self.step_by_step_on_nodes(counter_)
            if node.value == sub:
                counter_ += 1
                sum_ += 1
            else:
                counter_ += 1
        return sum_

    def extend(self, value: list) -> None:
        """ Добавление всех элементов списка в конец связного списка. """
        if not isinstance(value, list):
            raise TypeError('не список')
        for k in range(len(value)):
            self.append(value[k])

    def pop(self, index: int = None) -> Any:
        """ удаляет элемент из списка и возвращает элемент """
        if index is None:
            node = self.step_by_step_on_nodes(self._len - 1)
            self._len -= 1
            return node.value
        else:
            node = self.step_by_step_on_nodes(index)
            self.__delitem__(index)
            return node.value


class DoubleLinkedList(LinkedList):
    @staticmethod
    def _linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.
        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node
        right_node.prev = left_node

    def _init_linked_list(self, data: Iterable) -> None:
        """ Метод, который создает вспомогательный список и связывает в нём узлы. """
        self.list_nodes = [DoubleLinkedNode(value) for value in data]
        self._head = self.list_nodes[0]
        self._len = len(self.list_nodes)
        for j in range(len(self.list_nodes) - 1):
            current_node = self.list_nodes[j]
            next_node = self.list_nodes[j + 1]
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

    def insert(self, index: int, value: Any) -> None:
        """ Метод вставляет узел по указанному индексу"""
        if not isinstance(index, int):
            raise TypeError('в insert  не int')
        if not 0 <= index < self._len:  # для for
            raise IndexError('в insert  не тот индекс')
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
    print('к односвязному и двусвязному списку применяем insert и печатаем:')
    ll.insert(1, 9)
    dll.insert(1, 9)
    print(ll)
    print(dll)
    print('в односвязном и двусвязном списке c append проверяем как связаны узлы и листнодес это не показывает:')
    print(ll.list_nodes)
    print(dll.list_nodes)
    print('проверяем что узлы связаны корректно в обоих списках после применения инсёрт и апенд:')
    for i in range(len(ll)):
        print(repr(ll.step_by_step_on_nodes(i)))
    for i in range(len(dll)):
        print(repr(dll.step_by_step_on_nodes(i)))
    print('к односвязному и двусвязному списку применяем index и печатаем (середина, начало, конец):')
    print(ll.index('b'))
    print(dll.index('b'))
    print(ll.index('a'))
    print(dll.index('a'))
    print(ll.index('t'))
    print(dll.index('t'))
    print('к двусвязному списку применяем index c условием промежутка:')
    print(dll.index('b', 0, 3))
    # print(dll.index('b', 3, 5)) # ошибка
    print('к обоим спискам применяем сount:')
    print(ll.count('a'))
    print(dll.count('a'))
    print(ll.count('no'))
    print(dll.count('no'))
    print('к обоим спискам добавляем элемент и применяем сount:')
    ll.append(5)
    dll.append(5)
    print(ll.count(5))
    print(dll.count(5))
    print('к обоим спискам применяем extend и count:')
    List_extend = [5, 'yo', 5, 6]
    ll.extend(List_extend)
    dll.extend(List_extend)
    print(ll)
    print(dll)
    print(ll.count(5))
    print(dll.count(5))
    print('к обоим спискам применяем pop и печатаем списки:')
    print(ll)
    print(dll)
    print(ll.pop(2))
    print(dll.pop(2))
    print(ll)
    print(dll)
    print(ll.pop())
    print(dll.pop())
    print(ll)
    print(dll)
    print(ll.pop(0))
    print(dll.pop(0))
    print(ll)
    print(dll)
    print(repr(ll))
