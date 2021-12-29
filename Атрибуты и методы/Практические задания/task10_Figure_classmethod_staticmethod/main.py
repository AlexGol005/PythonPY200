import math


class TriangleCalculator:
    """ Класс-калькулятор площадей треугольников. """

    @classmethod
    def area(cls, *args): #self заменилим на cls
        """
        Метод, который считает площадь по разным формулам,
         в зависимости от количества переданных аргументов.
        """
        if len(args) == 2:
            cls.area_by_height(*args)
        if len(args) == 3:
            cls.area_by_angle(*args)

    @staticmethod
    def area_by_angle(a, b, angle):  #выкинули селф из аргументов сделали метод статическим, так как свойства калькулятора существуют вне экземпляра
        """ Формула площади по двум сторонам и углу между ними. """
        return 0.5 * a * b * math.sin(angle)



    @staticmethod
    def area_by_height(a, h):  #выкинули селф сделали метод статическим, так как свойства калькулятора существуют вне экземпляра
        """ Формула площади по основанию и высоте. """
        return 0.5 * a * h


if __name__ == '__main__':
    TriangleCalculator().area()  # Работаем через экземпляр
    TriangleCalculator().area_by_height(5, 10)  # Работаем через экземпляр

    TriangleCalculator.area()  # Работаем через класс
    TriangleCalculator.area_by_height(5, 10)  # Работаем через класс (метод стал статическим и ошибка исчезла)
    # статические методы работаю как от экземпляров, так и от класса
