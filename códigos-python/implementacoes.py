import math
import time
from time import perf_counter

# ==========================================
# FUNÇÕES DA QUESTÃO 1
# ==========================================
def f1(x):
    return 20000 * (x * (1 + x)**6) / ((1 + x)**6 - 1) - 4000

def g1(x):
    return (((x+1)**6)-1)/(5*((x+1)**6))

def df1(x):
    return (20000 * ((x + 1)**6) + 120000 * x * ((x + 1)**5))/(((x+1)**6) - 1) - (120000 * x * ((x + 1)**11))/(((x+1)**6 - 1)**2)

# ==========================================
# FUNÇÕES DA QUESTÃO 2
# ==========================================
def f2(x):
    return 10 - 20 * (math.exp(-0.2 * x) - math.exp(-0.75 * x)) - 5

def df2(x):
    # Derivada corrigida (sinais e expoentes mantidos negativos)
    return 4 * math.exp(-0.2 * x) - 15 * math.exp(-0.75 * x)

def g2(x):
    # Isolamento de x corrigido para garantir a convergência |g'(x)| < 1
    return -(4/3) * math.log(math.exp(-0.2 * x) - 0.25)

# ==========================================
# FUNÇÕES DA QUESTÃO 3
# ==========================================
def f3(x):
    return 2200 * math.log(160000 / (160000 - 2680 * x)) - 9.8 * x - 1000

# ==========================================
# FUNÇÕES DA QUESTÃO 0 (PADRÃO)
# ==========================================
def f(x):
    return x * math.log(x) - 1

def df(x):
    return math.log(x) + 1

def g(x):
    # Isolamento de x corrigido (x = e^(1/x)) para garantir convergência
    return math.exp(1 / x)

# ==========================================
# MÉTODOS NUMÉRICOS
# ==========================================
def bissecao(f, a, b, tol):
    start_time = perf_counter()
    iteracoes = 0
    c = (a + b) / 2  # Corrigido: inicia c no meio do intervalo 
    while abs(b - a) > tol:
        iteracoes += 1
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        print(f"Iteração = {iteracoes:02d}, a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, f(c) = {f(c):.4f}")
    raiz = c
    end_time = perf_counter()
    return raiz, iteracoes, (end_time - start_time) * 1000

def regula_falsi(f, a, b, tol):
    start_time = perf_counter()
    prev_c = 0
    iteracoes = 0
    while True:
        iteracoes += 1
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print(f"Iteração = {iteracoes:02d}, a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, f(c) = {f(c):.4f}")
        if abs(c - prev_c) < tol:
            break
        prev_c = c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    end_time = perf_counter()
    return c, iteracoes, (end_time - start_time) * 1000

def ponto_fixo(g, f, x0, tol=0.02, max_iter=100):
    start_time = perf_counter()
    x_atual = x0
    erro = 100
    iteracoes = 0

    # TRAVA DE SEGURANÇA: iteracoes < max_iter impede loop infinito
    while erro >= tol and iteracoes < max_iter:
        iteracoes += 1
        x_novo = g(x_atual)
        erro = abs(x_novo - x_atual)

        print(f"Iteração = {iteracoes:02d}, x_n = {x_atual:.4f}, x_n+1 = {x_novo:.4f}, f(x_n) = {f(x_atual):.4f}, f(x_n+1) = {f(x_novo):.4f}, Erro = {erro:.4f}")
        
        x_atual = x_novo

    if iteracoes >= max_iter:
        print("  -> ALERTA: O método atingiu o limite de iterações e pode não ter convergido.")

    raiz = x_atual
    end_time = perf_counter()
    return raiz, iteracoes, (end_time - start_time) * 1000

def newton_raphson(f, df, x0, tol=0.02, max_iter=100):
    start_time = perf_counter()
    x_atual = x0
    iteracoes = 0
    erro = 100

    # TRAVA DE SEGURANÇA adicionada aqui também
    while erro >= tol and iteracoes < max_iter:
        iteracoes += 1
        fx = f(x_atual)
        dfx = df(x_atual)

        if dfx == 0:
            raise ZeroDivisionError("A derivada zerou. O método não pode continuar.")

        x_novo = x_atual - (fx / dfx)
        erro = abs(x_novo - x_atual)

        print(f"Iteração = {iteracoes:02d}, x_n = {x_atual:.4f}, x_n+1 = {x_novo:.4f}, f(x_n) = {f(x_atual):.4f}, f(x_n+1) = {f(x_novo):.4f}, Erro = {erro:.4f}")
        x_atual = x_novo
    
    if iteracoes >= max_iter:
        print("  -> ALERTA: O método atingiu o limite de iterações e pode não ter convergido.")

    raiz = x_atual
    end_time = perf_counter()
    return raiz, iteracoes, (end_time - start_time) * 1000

# ==========================================
# INTERFACE PRINCIPAL
# ==========================================
print("==========================================================================================================")
print("Padrão 0")

print("\nQuestão 1: \nUm certo equipamento de 20.000 euros vai ser pago durante 6 anos através de pagamentos anuais de 4.000 euros. \nSabendo que a relação entre o custo P, o pagamento anual A, o número de anos n e a taxa de juro i é dada por \nA = P*(i(1+i)^n)/((1+i)^n -1 ), determine a taxa de juro utilizada sabendo que ela pertence ao intervalo [0.05, 0.15].")

print("\nQuestão 2: \nA equação c(x) = 10 - 20*(e^(-0.2x) - e^(-0.75x)) é usada para calcular a concentração de oxigênio em um rio. \nDetermine a distância x (no intervalo [0.1, 2.0]) para a qual o nível de oxigênio desce exatamente para o valor 5.")

print("\nQuestão 3: \nA velocidade de um foguete é v = 2200*ln(160000 / (160000 - 2680*t)) - 9.8*t. \nCalcule o tempo t necessário (no intervalo [20, 30]) para o foguete atingir a velocidade de 1000 m/s.")
print("==========================================================================================================")

controle = int(input("\nQual questão você quer executar (0, 1, 2 ou 3)? "))

if controle == 0:
    print("\n" + "-"*50)
    print("Método da Bisseção:")
    raiz_bis, it_bis, tempo_ms = bissecao(f, 1, 3, 0.02)
    print(f"f(x) = x * ln(x) - 1 | f(x) = 0 <=> x ≈ {raiz_bis:.4f} ({it_bis} iterações) (Tempo: {tempo_ms:.4f} ms)")
    
    print("\n" + "-"*50)
    print("Método da Falsa Posição:")
    raiz_rf, it_rf, tempo_ms = regula_falsi(f, 1, 3, 0.02)
    print(f"f(x) = x * ln(x) - 1 | f(x) = 0 <=> x ≈ {raiz_rf:.4f} ({it_rf} iterações) (Tempo: {tempo_ms:.4f} ms)")
    
    print("\n" + "-"*50)
    print("Método do Ponto Fixo:")
    raiz_pf, it_pf, tempo_ms = ponto_fixo(g, f, 1.2, 0.02)
    print(f"f(x) = x * ln(x) - 1 | f(x) = 0 <=> x ≈ {raiz_pf:.4f} ({it_pf} iterações) (Tempo: {tempo_ms:.4f} ms)")
    
    print("\n" + "-"*50)
    print("Método de Newton-Raphson:")
    raiz_nr, it_nr, tempo_ms = newton_raphson(f, df, 1.5, 0.02)
    print(f"f(x) = x * ln(x) - 1 | f(x) = 0 <=> x ≈ {raiz_nr:.4f} ({it_nr} iterações) (Tempo: {tempo_ms:.4f} ms)\n")

elif controle == 1:
    print("\n" + "-"*50)
    print("Método da Bisseção:")
    raiz_bis, it_bis, tempo_ms = bissecao(f1, 0.05, 0.15, 0.0001)
    print(f"f(i) = 0 <=> i = {raiz_bis:.4f} ({it_bis} iterações) (Tempo: {tempo_ms:.4f} ms)")
    
    print("\n" + "-"*50)
    print("Método da Falsa Posição:")
    raiz_rf, it_rf, tempo_ms = regula_falsi(f1, 0.05, 0.15, 0.0001)
    print(f"f(i) = 0 <=> i = {raiz_rf:.4f} ({it_rf} iterações) (Tempo: {tempo_ms:.4f} ms)")
    
    print("\n" + "-"*50)
    print("Método do Ponto Fixo:")
    raiz_pf, it_pf, tempo_ms = ponto_fixo(g1, f1, 0.05, 0.0001)
    print(f"f(i) = 0 <=> i = {raiz_pf:.4f} ({it_pf} iterações) (Tempo: {tempo_ms:.4f} ms)")
    
    print("\n" + "-"*50)
    print("Método de Newton-Raphson:")
    raiz_nr, it_nr, tempo_ms = newton_raphson(f1, df1, 0.05, 0.0001)
    print(f"f(i) = 0 <=> i = {raiz_nr:.4f} ({it_nr} iterações) (Tempo: {tempo_ms:.4f} ms)\n")

elif controle == 2:
    print("\n" + "-"*50)
    print("Método da Bisseção:")
    raiz_bis, it_bis, tempo_ms = bissecao(f2, 0.1, 2.0, 0.001)
    print(f"f(x) = 0 <=> x = {raiz_bis:.4f} ({it_bis} iterações) (Tempo: {tempo_ms:.4f} ms)")
    
    print("\n" + "-"*50)
    print("Método da Falsa Posição:")
    raiz_rf, it_rf, tempo_ms = regula_falsi(f2, 0.1, 2.0, 0.001)
    print(f"f(x) = 0 <=> x = {raiz_rf:.4f} ({it_rf} iterações) (Tempo: {tempo_ms:.4f} ms)")
    
    print("\n" + "-"*50)
    print("Método do Ponto Fixo:")
    raiz_pf, it_pf, tempo_ms = ponto_fixo(g2, f2, 0.75, 0.001)
    print(f"f(x) = 0 <=> x = {raiz_pf:.4f} ({it_pf} iterações) (Tempo: {tempo_ms:.4f} ms)")
    
    print("\n" + "-"*50)
    print("Método de Newton-Raphson:")
    raiz_nr, it_nr, tempo_ms = newton_raphson(f2, df2, 1.2, 0.001)
    print(f"f(x) = 0 <=> x = {raiz_nr:.4f} ({it_nr} iterações) (Tempo: {tempo_ms:.4f} ms)\n")

elif controle == 3:
    print("\n" + "-"*50)
    print("Método da Bisseção:")
    raiz_bis, it_bis, tempo_ms = bissecao(f3, 20, 30, 0.01)
    print(f"f(t) = 0 <=> t = {raiz_bis:.4f} ({it_bis} iterações) (Tempo: {tempo_ms:.4f} ms)")
    
    print("\n" + "-"*50)
    print("Método da Falsa Posição:")
    raiz_rf, it_rf, tempo_ms = regula_falsi(f3, 20, 30, 0.01)
    print(f"f(t) = 0 <=> t = {raiz_rf:.4f} ({it_rf} iterações) (Tempo: {tempo_ms:.4f} ms)\n")

else:
    print(f"\nA questão {controle} não existe!")
    exit(1)
