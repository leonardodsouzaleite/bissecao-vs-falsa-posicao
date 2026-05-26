import math

def f1(x):
    return 20000 * (x * (1 + x)**6) / ((1 + x)**6 - 1) - 4000

def f2(x):
    return 10 - 20 * (math.exp(-0.2 * x) - math.exp(-0.75 * x)) - 5

def f3(x):
    return 2200 * math.log(160000 / (160000 - 2680 * x)) - 9.8 * x - 1000

def f(x):
    return x * math.log(x) - 1

def bissecao(f, a, b, tol):
    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def regula_falsi(f, a, b, tol):
    prev_c = 0
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(c - prev_c) < tol:
            break
        prev_c = c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c


print("==========================================================================================================")
print("Padrão 0")

print("\nQuestão 1: \nUm certo equipamento de 20.000 euros vai ser pago durante 6 anos através de pagamentos anuais de 4.000 euros. \nSabendo que a relação entre o custo P, o pagamento anual A, o número de anos n e a taxa de juro i é dada por \nA = P*(i(1+i)^n)/((1+i)^n -1 ), determine a taxa de juro utilizada sabendo que ela pertence ao intervalo [0.05, 0.15].")

print("\nQuestão 2: \nA equação c(x) = 10 - 20*(e^(-0.2x) - e^(-0.75x)) é usada para calcular a concentração de oxigênio em um rio. \nDetermine a distância x (no intervalo [0.1, 2.0]) para a qual o nível de oxigênio desce exatamente para o valor 5.")

print("\nQuestão 3: \nA velocidade de um foguetão é v = 2200*ln(160000 / (160000 - 2680*t)) - 9.8*t. \nCalcule o tempo t necessário (no intervalo [20, 30]) para o foguetão atingir a velocidade de 1000 m/s.")
print("==========================================================================================================")

controle = int(input("Qual questão você quer executar (0, 1, 2 ou 3)? "))

if controle == 0:
    print("\n")
    print("Método da Bisseção:\n    f(x) = x * log(x) - 1 | f(x) = 0 <=> x = ", bissecao(f, 1, 3, 0.02))
    print("\n")
    print("Método da Falsa Posição:\n    f(x) = x * log(x) - 1 | f(x) = 0 <=> x = ", regula_falsi(f, 1, 3, 0.02))
    print("\n")

if controle == 1:
    print("\n")
    print("Método da Bisseção:\n    f(i) = P*(i(1+i)^n)/((1+i)^n - 1) - A = 0 <=> i = ", bissecao(f1, 0.05, 0.15, 0.0001))
    print("\n")
    print("Método da Falsa Posição:\n    f(i) = P*(i(1+i)^n)/((1+i)^n - 1) - A = 0 <=> i = ", regula_falsi(f1, 0.05, 0.15, 0.0001))
    print("\n")

elif controle == 2:
    print("\n")
    print("Método da Bisseção:\n    f(x) = 10 - 20*(e^(-0.2x) - e^(-0.75x)) - 5 = 0 <=> x = ", bissecao(f2, 0.1, 2.0, 0.001))
    print("\n")
    print("Método da Falsa Posição:\n    f(x) = 10 - 20*(e^(-0.2x) - e^(-0.75x)) - 5 = 0 <=> x = ", regula_falsi(f2, 0.1, 2.0, 0.001))
    print("\n")

elif controle == 3:
    print("\n")
    print("Método da Bisseção:\n    f(t) = 2200*ln(160000 / (160000 - 2680*t)) - 9.8*t - 1000 = 0 <=> t = ", bissecao(f3, 20, 30, 0.01))
    print("\n")
    print("Método da Falsa Posição:\n    f(t) = 2200*ln(160000 / (160000 - 2680*t)) - 9.8*t - 1000 = 0 <=> t = ", regula_falsi(f3, 20, 30, 0.01))
    print("\n")