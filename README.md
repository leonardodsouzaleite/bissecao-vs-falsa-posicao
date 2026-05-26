# 📐 Bisseção vs Falsa Posição

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Manim](https://img.shields.io/badge/Manim-Animation-green?style=for-the-badge)
![NumPy](https://img.shields.io/badge/NumPy-Math-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

Projeto desenvolvido em **Python + Manim** para visualizar e comparar os métodos numéricos da:

### 🔵 Bisseção

### 🟠 Falsa Posição

</div>

---

# 🎯 Objetivo

Este projeto foi criado para demonstrar visualmente o funcionamento de dois métodos clássicos de aproximação de raízes:

- 🔵 Método da **Bisseção**
- 🟠 Método da **Falsa Posição**

A função analisada é:

```math
f(x) = x \cdot ln(x) - 1
```

com critério de parada:

```math
|f(c)| < 0.02
```

---

# 🧠 O que o projeto mostra

## 🔵 Método da Bisseção

- Divide o intervalo ao meio repetidamente
- Extremamente estável
- Simples de implementar
- Convergência garantida

## 🟠 Método da Falsa Posição

- Usa interpolação linear
- Geralmente converge mais rápido
- Mantém o intervalo válido
- Não utiliza derivadas

---

# 🎬 Animações

As animações foram desenvolvidas usando o **Manim Community**.

Cada método possui:

- gráfico da função;
- atualização visual do intervalo;
- aproximações sucessivas;
- exibição dos pontos importantes;
- critério de parada;
- comparação de convergência.

---

# 📁 Estrutura do projeto

```text
bissecao-vs-falsa-posicao/
│
├── códigos-python/
│   ├── bissecao.py
│   ├── falsa_posicao.py
│   ├── comparacao_codigo.py
│   └── comparacao_metodos.py
│
├── Metodo-da-Falsa-Posicao.pdf
└── README.md
```

---

# ⚙️ Tecnologias utilizadas

| Tecnologia | Função                |
| ---------- | --------------------- |
| Python     | Linguagem principal   |
| Manim      | Criação das animações |
| NumPy      | Operações matemáticas |
| LaTeX      | Fórmulas matemáticas  |

---

# 🚀 Como executar

## 1️⃣ Clonar o repositório

```bash
git clone https://github.com/leonardodsouzaleite/bissecao-vs-falsa-posicao.git
cd bissecao-vs-falsa-posicao/códigos-python
```

---

## 2️⃣ Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3️⃣ Instalar dependências

```bash
pip install manim numpy
```

---

## 4️⃣ Renderizar animações

### 🔵 Bisseção

```bash
manim -pqh comparacao_metodos.py BissecaoScene
```

### 🟠 Falsa Posição

```bash
manim -pqh comparacao_metodos.py FalsaPosicaoScene
```

### 🎬 Ambas

```bash
manim -pqh comparacao_metodos.py BissecaoScene FalsaPosicaoScene
```

---

# 📊 Resultado

O projeto gera vídeos comparando visualmente os dois métodos numéricos.

A animação evidencia:

- comportamento iterativo;
- redução do intervalo;
- velocidade de convergência;
- diferenças entre os métodos.

---

# 📚 Finalidade acadêmica

Projeto desenvolvido para fins didáticos e acadêmicos na disciplina de **Cálculo Numérico**.
