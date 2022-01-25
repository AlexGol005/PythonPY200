import unittest

from task import Node


class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(5)
        #self.assertIs(None, node.next)
        self.assertIsNone(node.next)
        self.assertEqual(5, node.value)
        # TODO с помощью метода assertIsNone проверить следующий узел

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        right_node = Node('right')
        left_node = Node('left', next_=right_node)
        self.assertIs(right_node, left_node.next)
        self.assertIsNone(right_node.next)
        self.assertEqual('left', left_node.value)
        self.assertEqual('right', right_node.value)
        # TODO проверить что узлы связались

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node = Node(5)
        expected_repr = "Node(5, None)"
        self.assertEqual(expected_repr, repr(node), )
          # TODO проверить метод __repr__ без следующего узла

     # TODO пропустить тест с помощью декоратора unittest.skip
    @unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        node = Node(5, Node(10))
        expected_repr = "Node(5, None)"
        self.assertEqual(expected_repr, repr(node), msg='Неправильный __repr__')

    def test_str(self):
        some_value = 5
        node = Node(some_value)
        self.assertEqual(str(node), str(some_value))

        # TODO проверить строковое представление

    def test_is_valid(self):
        Node.is_valid(None)
        Node.is_valid(Node(5))
        with self.assertRaises(TypeError):
            Node.is_valid(5)
        # TODO проверить метод is_valid при корректных узлах

        # TODO с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
