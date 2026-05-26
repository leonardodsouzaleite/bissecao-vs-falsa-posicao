import numpy as np
import matplotlib.pyplot as plt
import time

def f(x):
    return x * np.log(x) - 1

def bissecao(a, b, tol=0.02, pausa=0.8):
    if f(a) * f(b) >= 0:
        print("Intervalo inválido")
        return None
    
    pontos = []
    
    plt.figure(figsize=(10,6))
    x_curva = np.linspace(0.5, 3, 400)
    y_curva = f(x_curva)
    plt.plot(x_curva, y_curva, 'b-', linewidth=2)
    plt.axhline(0, color='k', linestyle='--')
    plt.grid(True, alpha=0.3)
    plt.title("Método da Bisseção")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    
    i = 0
    while abs(b - a) > tol:
        c = (a + b) / 2
        pontos.append(c)
        print(f"Iteração {i+1}: x = {c:.6f}")
        
        plt.scatter(c, f(c), color='red', s=80)
        plt.annotate(f"{i+1}", (c, f(c)), xytext=(8,8), textcoords='offset points')
        plt.draw()
        plt.pause(pausa)
        
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        i += 1
    
    plt.scatter(c, f(c), color='green', s=150, marker='*')
    plt.legend(["f(x)", "raiz"], loc="upper right")
    plt.show()
    
    return c

# Executar
raiz = bissecao(1, 3, tol=0.02, pausa=0.8)
print(f"\nRaiz aproximada: {raiz:.6f}")
