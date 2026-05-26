import numpy as np
import matplotlib.pyplot as plt
import time


def f(x):
    return x * np.log(x) - 1


def falsa_posicao(a, b, tol=0.02, pausa=0.8):
    if f(a) * f(b) >= 0:
        print("Intervalo inválido")
        return None

    pontos = []
    fa = f(a)
    fb = f(b)

    plt.figure(figsize=(10, 6))
    x_curva = np.linspace(0.5, 3, 400)
    y_curva = f(x_curva)
    plt.plot(x_curva, y_curva, "b-", linewidth=2)
    plt.axhline(0, color="k", linestyle="--")
    plt.grid(True, alpha=0.3)
    plt.title("Método da Falsa Posição (Illinois)")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    i = 0
    lado_anterior = None

    while abs(b - a) > tol and i < 50:
        # Fórmula da falsa posição
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        pontos.append(c)
        print(f"Iteração {i + 1}: x = {c:.6f} | Diferença (b-a) = {abs(b - a)} > {tol}")

        plt.scatter(c, fc, color="red", s=80)
        plt.annotate(f"{i + 1}", (c, fc), xytext=(8, 8), textcoords="offset points")
        plt.draw()
        plt.pause(pausa)

        if abs(fc) < 1e-12:
            break

        # Critério de Illinois: se o sinal se repete no mesmo lado, reduz o peso da função
        if fa * fc < 0:
            # Raiz entre a e c
            if lado_anterior == "direito":
                fa = fa * 0.5  # reduz o valor de f(a) pra acelerar
            b = c
            fb = fc
            lado_anterior = "direito"
        else:
            # Raiz entre c e b
            if lado_anterior == "esquerdo":
                fb = fb * 0.5
            a = c
            fa = fc
            lado_anterior = "esquerdo"

        i += 1

    raiz = c
    plt.scatter(raiz, f(raiz), color="green", s=150, marker="*")
    plt.legend(["f(x)", "raiz"], loc="upper right")
    plt.show()

    return raiz, abs(b - a), tol


# Execução
raiz, diferenca, parada = falsa_posicao(1, 3, tol=0.02, pausa=0.02)
print(f"\nRaiz aproximada: {raiz:.6f} | Diferença (b - a) = {diferenca} <= {parada}")
