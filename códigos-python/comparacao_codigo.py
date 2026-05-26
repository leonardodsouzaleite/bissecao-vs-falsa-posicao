import numpy as np

def f(x):
    return x * np.log(x) - 1

def bissecao_slide(f, a, b, tol=0.02):
    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def regula_falsi_slide(f, a, b, tol=0.02):
    prev_c = a + 100
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(c - prev_c) < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        prev_c = c
    return c

# Execução dos testes
print(f"Raiz (Bisseção Slide): {bissecao_slide(f, 1, 3):.6f}")
print(f"Raiz (Falsa Posição Slide): {regula_falsi_slide(f, 1, 3):.6f}")
