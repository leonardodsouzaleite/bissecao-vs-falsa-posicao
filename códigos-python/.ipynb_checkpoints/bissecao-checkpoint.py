import numpy as np
import matplotlib.pyplot as plt

# Função
def f(x):
    return x * np.log(x) - 1


# Método da Bisseção
def bissecao(a, b, tol=0.02):

    iteracoes = []

    if f(a) * f(b) >= 0:
        print("Intervalo inválido")
        return

    i = 0

    while abs(b - a) > tol:

        c = (a + b) / 2

        iteracoes.append(c)

        print(f"Iteração {i+1}: x = {c:.6f}")

        if f(c) == 0:
            break

        elif f(a) * f(c) < 0:
            b = c

        else:
            a = c

        i += 1

    return c, iteracoes


# Executando
raiz, pontos = bissecao(1, 3)

print("\nRaiz aproximada:", raiz)


# Gráfico
x = np.linspace(0.5, 3, 400)
y = f(x)

plt.figure(figsize=(10,6))

plt.plot(x, y, label='f(x) = x ln(x) - 1')
plt.axhline(0)

# Aproximações
for i, p in enumerate(pontos):
    plt.scatter(p, f(p), label=f'Iter {i+1}')

plt.title('Método da Bisseção')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()

plt.show()