import unittest

from task import DoubleLinkedList, LinkedList


class LinkedListTest(unittest.TestCase):

    def test_str_dll(self):
        """Проверить метод str для односвязного списка"""
        some_value = [5, 6, 7]
        dll = DoubleLinkedList(some_value)
        self.assertEqual(str(dll), str(some_value))

    def test_get_ll(self):
        """Проверить метод __getitem__ для односвязного списка"""
        ll = LinkedList(['a', 'b', 'c'])
        self.assertIs('b', ll.__getitem__(1))

    @unittest.skip("fix pop")
    def test_pop(self):
        ll = LinkedList([1, 2, 3])

        ll.pop()
        self.assertEqual(str([1, 2]), str(ll))
        self.assertEqual(2, len(ll))

        current_value = ll._head
        for _ in range(3):
            print(current_value)
            current_value = current_value.next

    def test_set_ll(self):  # если не использовать стр то и из и иквал выдают ошибку!
        """Проверить метод __setitem__ для односвязного списка"""
        ll = LinkedList(['a', 'b', 'c'])
        ll.__setitem__(1, 's')
        self.assertEqual("['a', 's', 'c']", str(ll))

    def test_delitem_ll(self):
        """Проверить метод __delitem__ для односвязного списка"""
        ll = LinkedList(['a', 's', 'c'])
        ll.__delitem__(1)
        self.assertEqual(str(LinkedList(['a', 'c'])), str(ll))

    def test_len_ll(self):
        """Проверить метод __len__ для односвязного списка"""
        ll = LinkedList(['a', 's', 'c'])
        self.assertEqual(3, ll.__len__())

    def test_len_ll(self):
        """Проверить метод __len__ для односвязного списка"""
        ll = LinkedList(['a', 's', 'c'])
        self.assertEqual(3, ll.__len__())

    def test_len_ll_zero(self):  # если от пустого списка, то выдаёт ошибку!
        """Проверить метод __len__ для пустого односвязного списка"""
        ll = LinkedList()
        self.assertEqual(0, ll.__len__())

    def test_repr_ll(self):
        """Проверить метод __repr__ для  односвязного списка"""
        some_value = ['a', 'b', 'c']
        ll = LinkedList(some_value)
        self.assertEqual(repr(ll), "LinkedList(['a', 'b', 'c'])")

    def test_insert_ll(self):
        """Проверить метод insert для  односвязного списка"""
        ll = LinkedList(['a', 'b', 'c'])
        ll.insert(1, 's')
        self.assertEqual(str(['a', 's', 'b', 'c']), str(ll))

    def test_insert_ll_max(self):
        """Проверить метод insert для макасимального индекса для  односвязного списка"""
        ll = LinkedList(['a', 'b', 'c'])
        ll.insert(2, 's')
        self.assertEqual(str(['a', 'b', 's', 'c']), str(ll))

    def test_insert_ll_zero(self):
        """Проверить метод insert для нулевого индекса для  односвязного списка"""
        ll = LinkedList(['a', 'b', 'c'])
        ll.insert(0, 's')
        self.assertEqual(str(['s', 'a', 'b', 'c']), str(ll))

    def test_append_ll(self):
        """Проверить метод аппенд для непустого односвязного списка"""
        ll = LinkedList(['a', 'b', 'c'])
        ll.append('s')
        self.assertEqual(str(['a', 'b', 'c', 's']), str(ll))

    def test_append_ll_none(self):
        """Проверить метод аппенд для пустого односвязного списка"""
        ll = LinkedList()
        ll.append('s')
        self.assertEqual(str(['s']), str(ll))

    def test_index_ll(self):
        """Проверить метод index для  односвязного списка"""
        ll = LinkedList(['a', 'b', 'c'])
        self.assertEqual(1, ll.index('b'))

    def test_step_by_step_on_nodes_ll(self):  # почему степ бай степ в самом файле печатает вид узлов только через репр,
        # приходится брать строку чтобы получить значение
        """Проверить метод step_by_step_on_nodes для  односвязного списка"""
        ll = LinkedList(['a', 'b', 'c'])
        self.assertEqual('b', str(ll.step_by_step_on_nodes(1)))

    def test_leftnode_ll(self):
        """Проверить вид первого узла для односвязного списка"""
        ll = LinkedList(['a', 'b', 'c'])
        self.assertEqual('Node(a, Node(b))', repr(ll.step_by_step_on_nodes(0)))

    def test_rightnode_ll(self):
        """Проверить вид последнего узла для односвязного списка"""
        ll = LinkedList(['a', 'b', 'c'])
        self.assertEqual('Node(c, None)', repr(ll.step_by_step_on_nodes(2)))


class DoubleLinkedListTest(unittest.TestCase):

    def test_str_ll(self):
        """Проверить метод str для двусвязного списка"""
        some_value = [5, 6, 7]
        dll = LinkedList(some_value)
        self.assertEqual(str(dll), str(some_value))

    def test_get_dll(self):
        """Проверить метод __getitem__ для двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertIs('b', dll.__getitem__(1))

    def test_set_dll(self):
        """Проверить метод __setitem__ для двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        dll.__setitem__(1, 's')
        self.assertEqual(str(DoubleLinkedList(['a', 's', 'c'])), str(dll))

    def test_delitem_dll(self):
        """Проверить метод __delitem__ для двусвязного списка"""
        dll = LinkedList(['a', 's', 'c'])
        dll.__delitem__(1)
        self.assertEqual(str(DoubleLinkedList(['a', 'c'])), str(dll))

    def test_len_dll(self):
        """Проверить метод __delitem__ для двусвязного списка"""
        dll = DoubleLinkedList(['a', 's', 'c'])
        self.assertEqual(3, dll.__len__())

    def test_len_dll_zero(self):  # если от пустого списка, то выдаёт ошибку!
        """Проверить метод __delitem__ для пустого двусвязного списка"""
        dll = DoubleLinkedList()
        self.assertEqual(0, dll.__len__())

    def test_repr_dll(self):
        """Проверить метод __repr__ для  двусвязного списка"""
        some_value = ['a', 'b', 'c']
        dll = DoubleLinkedList(some_value)
        self.assertEqual(repr(dll), "DoubleLinkedList(['a', 'b', 'c'])")

    def test_insert_dll(self):
        """Проверить метод insert для  двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        dll.insert(1, 's')
        self.assertEqual(str(['a', 's', 'b', 'c']), str(dll))

    def test_insert_dll_zero(self):
        """Проверить метод insert для нулевого индекса для  двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        dll.insert(0, 's')
        self.assertEqual(str(['s', 'a', 'b', 'c']), str(dll))

    def test_insert_dll_max(self):
        """Проверить метод insert для макасимального индекса для  двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        dll.insert(2, 's')
        self.assertEqual(str(['a', 'b', 's', 'c']), str(dll))

    def test_append_dll(self):
        """Проверить метод аппенд для непустого двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        dll.append('s')
        self.assertEqual(str(['a', 'b', 'c', 's']), str(dll))

    def test_append_dll_none(self):
        """Проверить метод аппенд для пустого двусвязного списка"""
        dll = DoubleLinkedList()
        dll.append('s')
        self.assertEqual(str(['s']), str(dll))

    def test_index_dll(self):
        """Проверить метод index для  двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertEqual(1, dll.index('b'))

    def test_step_by_step_on_nodes_dll(self):
        """Проверить метод step_by_step_on_nodes для двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertEqual('b', str(dll.step_by_step_on_nodes(1)))

    def test_leftnode_dll(self):
        """Проверить вид первого узла для двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertEqual('DoubleLinkedNode(a, DoubleLinkedNode(b), None)', repr(dll.step_by_step_on_nodes(0)))

    def test_centralnode_dll(self):
        """Проверить вид среднего узла для двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertEqual('DoubleLinkedNode(b, DoubleLinkedNode(c), DoubleLinkedNode(a))',
                         repr(dll.step_by_step_on_nodes(1)))

    def test_rightnode_dll(self):
        """Проверить вид последнего узла для двусвязного списка"""
        dll = DoubleLinkedList(['a', 'b', 'c'])
        self.assertEqual('DoubleLinkedNode(c, None, DoubleLinkedNode(b))', repr(dll.step_by_step_on_nodes(2)))
