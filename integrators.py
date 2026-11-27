"""Модуль реалізації класів чисельного інтегрування."""


class BaseIntegrator:
    """Базовий клас для чисельного обчислення визначених інтегралів."""

    order = 1
    method_name = "Базовий метод"

    def __init__(self, func, a, b):
        """Ініціалізує підінтегральну функцію та межі інтегрування."""

        if not self.validate_bounds(a, b):
            print("Некоректні межі")
        self.func = func
        self.a = a
        self.b = b

    @classmethod
    def from_dict(cls, func, params):
        """Альтернативний конструктор для створення інтегратора зі словника."""

        return cls(func, params["a"], params["b"])

    @staticmethod
    def validate_bounds(a, b):
        """Перевіряє коректність меж інтегрування."""

        return a < b

    def integrate(self, n):
        """Обчислює наближене значення інтеграла для n розбиттів."""
        raise NotImplementedError

    def adaptive_integrate(self, eps=1e-4, initial_n=2):
        """Знаходить інтеграл із заданою точністю eps за правилом Рунге."""

        k = 2 ** self.order - 1
        n = initial_n
        previous = self.integrate(n)  
        history = [(n, previous)]
        while True:
            n *= 2  
            current = self.integrate(n)  
            history.append((n, current))
            d = abs(current - previous) / k
            if d <= eps:
                new = current + (current - previous) / k
                return new, n, d, history
            previous = current

    def __str__(self):
        """Повертає рядкове представлення об'єкта інтегратора."""

        return (f"{self.method_name} на відрізку [{self.a}; {self.b}] "
                f"(порядок точності O(h^{self.order}))")


class RectangleIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою середніх прямокутників."""

    order = 2
    method_name = "Формула прямокутників"

    def __init__(self, func, a, b):

        super().__init__(func, a, b)

    def integrate(self, n):

        h = (self.b - self.a) / n
        total = sum(self.func(self.a + i * h + h / 2) for i in range(n))
        return h * total


class TrapezoidIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою трапецій."""

    order = 2
    method_name = "Формула трапецій"

    def __init__(self, func, a, b):

        super().__init__(func, a, b)

    def integrate(self, n):

        h = (self.b - self.a) / n
        ends = (self.func(self.a) + self.func(self.b)) / 2
        total = sum(self.func(self.a + i * h) for i in range(1, n))
        return h * (ends + total)


class SimpsonIntegrator(BaseIntegrator):
    """Обчислення інтеграла складеною формулою Сімпсона."""

    order = None
    method_name = "Формула Сімпсона"

    def __init__(self, func, a, b):
        pass

    def integrate(self, n):
        pass
