"""Головний модуль запуску чисельного інтегрування."""

import math

from integrators import (
    RectangleIntegrator,
    SimpsonIntegrator,
    TrapezoidIntegrator,
)


def target_function(x):
    """Підінтегральна функція згідно з індивідуальним варіантом."""

    return math.cos(x + x ** 3)
    #return (math.cos(x) - 1) / (x**2 + 0.0000000000000001)

def main():
    """Точка входу програми."""

    parameters = {"a": 0.0, "b": 1.0}
    eps = 1e-4
    print(f"eps = {eps}")
    integrators = [RectangleIntegrator.from_dict(target_function, parameters),
                   TrapezoidIntegrator.from_dict(target_function, parameters),
                   SimpsonIntegrator.from_dict(target_function, parameters),]
    for integrator in integrators:
        print(integrator)
        value, n_min, d, history = integrator.adaptive_integrate(eps = eps)
        for n, partial in history:
            print(f" n = {n:<3} -> I = {partial:.7f}")
        print(f" Уточнений результат: {value:.7f} "
              f"(n_min = {n_min}, похибка: {d:.2e})\n")

if __name__ == "__main__":
    main()