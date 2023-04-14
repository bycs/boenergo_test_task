import math


def quadratic_equation(a: float, b: float, c: float) -> float | tuple[float, float] | None:
    """
    Функция для нахождения корней квадратного уравнения ax^2 + bx + c = 0.

    :param a: коэффициент при x^2
    :param b: коэффициент при x
    :param c: свободный коэффициент
    :return: корни уравнения в виде кортежа (x1, x2) или один корень в виде числа, если дискриминант
             равен 0, или None, если уравнение не имеет корней
    """
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
